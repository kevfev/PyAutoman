package automanlib;
import edu.umass.cs.automan.adapters.mturk.DSL._
import automanlib_rpc._;
import automanlib_rpc.AutomanTask.TaskType;
import automanlib_classes._;
import automanlib_wrappers._;
import scala.concurrent.{ ExecutionContext, Future };


object EstimationPrototypeServicer extends GrpcServer{ self => 
	private class EstimationServicer extends EstimationPrototypeGrpc.EstimationPrototype {
		private var _adptr_credentials: Option[AdapterCredentials] = None;
		
		/** rpc method used by client to submit a task to Automan.
			If adapter credentials are supplied, run the task if it is valid and return the outcome
			. If either the task is invalid or an adapter is not registered, set returnCode to 
			ERROR and setn error message appropriately
		*
		*  @param automanTask - submitted task
		*  @return a new TaskRespone instance with the outcome of the task. Check for any errors
		*				set in "return_code" field. If field is valid then outcome is valid, else
		*				an error occured
		*							
		*/
		def submitTask(automanTask: AutomanTask) : Future[TaskResponse] = {
			var response: TaskResponse = TaskResponse()
			println("Received Task")
			_adptr_credentials match {
				case Some(adptr) => 
					response = response.withReturnCode(TaskResponse.TaskReturnCode.VALID)
					automanTask.taskType match {
						case TaskType.EstTask(etask) =>
							println("Type: Estimation");
							response = response.withEstimateOutcome(estimateTask(etask.getTask, adptr));
						case TaskType.MestTask(metask) =>
							println("Type: Multiestimate");
							response = response.withMultiestimateOutcome(multiestimateTask(metask.getTask, adptr));
						case TaskType.FreeTask(frtask) =>
							println("Type: Freetext");
							response = response.withFreetextOutcome(freetextTask(frtask.getTask, adptr));
						case TaskType.FreeDistTask(frdtask) =>
							println("Type: FreetextDist");
							response = response.withFreetextDistOutcome(freetextDistTask(frdtask.getTask, adptr));
						case TaskType.RadioTask(rtask) =>
							println("Type: Radio");
							response = response.withRadioOutcome(radioTask(rtask.getTask, adptr));
						case TaskType.RadioDistTask(rdtask) =>
							println("Type: RadioDist") ;
							response = response.withRadioDistOutcome(radioDistTask(rdtask.getTask, adptr));
						case TaskType.CheckTask(chtask) =>
							println("Type: Checkbox");
							response = response.withCheckboxOutcome(checkboxTask(chtask.getTask, adptr));
						case TaskType.CheckDistTask(chdtask) =>
							println("Type: CheckboxDist");
							response = response.withCheckboxDistOutcome(checkboxDistTask(chdtask.getTask, adptr));
						case TaskType.Empty=>
							println("ERROR: Empty Task ");
							response =response.withReturnCode(TaskResponse.TaskReturnCode.ERROR)
										.withErrMsg("ERROR: Empty Task. Refer to rpc API for a list of task types and usage"); 
						case _ =>
							println("ERROR: Task Type Unknown.");
							response =response.withReturnCode(TaskResponse.TaskReturnCode.ERROR)
										.withErrMsg("ERROR: Task Type Unknown. Refer to rpc API for a list of task types"); 
						}
				case _ => 
					println("ERROR: no credentials registered");
					response =response.withReturnCode(TaskResponse.TaskReturnCode.ERROR)
								.withErrMsg("ERROR: no crowdsource adapter credentials registered"); 
					
			}
			val tr: TaskResponse = response;
			Future.successful(tr);
		}

		/** internal method used by server, submits an estimate task to Automan
		*
		*  @param task - submitted task
		*  @param adptr - adapter with credentials to connect to the crowdsource back-end
		*  @return a new EstimateOutcome, representing the outcome of the task. 
		*							
		*/
		def estimateTask(task : Task, adptr: AdapterCredentials) : EstimateOutcome = {
			/** private method used by estimateTask to make and EstimateOutcome with ValueOutcome message field set
			*
			*  @param _est - estimate returned by AutoMan
			*  @param _low - lowest worker response
			*  @param _high - highest worker response
			*  @param _cost - cost of task
			*  @param _conf - confidence of result
			*  @return an EstimateOutcome with all fields but outcomeType initialized
			*							
			*/
			def _makeValueOutcome( _est : BigDecimal, _low : BigDecimal, _high: BigDecimal, _cost: BigDecimal, _conf: BigDecimal): EstimateOutcome = {
				return EstimateOutcome().withAnswer(ValueOutcome(est = _est.toDouble,low = _low.toDouble,high = _high.toDouble,cost = _cost.toDouble,conf = _conf.toDouble))
										.withNeed(-1.0)
										.withHave(-1.0);
			}

			/** private method used by estimateTask to make an overbudget EstimateOutcome
			*
			*  @param _need - the amount needed by AutoMan to continue trying the task
			*  @param _have - the amount originally allocated for the task
			*  @return an EstimateOutcome for an overbudget result
			*							
			*/
			def _makeOverBudgetOutcome( _need: BigDecimal, _have: BigDecimal): EstimateOutcome = {
				return EstimateOutcome().withOutcomeType(OutcomeType.OVERBUDGET)
										.withNeed(_need.toDouble)
										.withHave(_have.toDouble);
			}

			implicit val mt = mturk (
			   access_key_id = adptr.accessId,
			   secret_access_key = adptr.accessKey,
			   sandbox_mode = adptr.adapterOptions("sandbox_mode").toBoolean
			)
			
			/**private method used by estimateTask to run an AutoMan estimation task
			*/			
			def est(title_ : String ,text_ : String, budget_ : Double, image_url_ : String, def_samp_size: Int = -1, ques_timeout_mult: Int = 500) = estimate(
				default_sample_size = def_samp_size,
				text = text_ ,
				title = title_ ,
				image_url = image_url_ ,
				budget = budget_ ,
				question_timeout_multiplier = ques_timeout_mult
			)
			
			/* Run the task using AutoMan and then package the result appropriately depending on the 
			type of outcome.
			*/
			automan(mt) {
				val automan_outcome = est(title_ = task.title, text_ =task.text, budget_ =task.budget, image_url_ =task.imgUrl, ques_timeout_mult=3, def_samp_size=2);
				var outcome = EstimateOutcome()
				automan_outcome.answer match{
					case Estimate(est, low, high, cost, conf, _, _) => 
						println("estimated,"); 
						outcome = _makeValueOutcome(est, low, high, cost, conf).withOutcomeType(OutcomeType.CONFIDENT);
					case LowConfidenceEstimate(est, low, high, cost, conf, _, _) => 
						println("low conf estimated,");
						outcome = _makeValueOutcome(est, low, high, cost, conf).withOutcomeType(OutcomeType.LOW_CONFIDENCE);
					case OverBudgetEstimate(need, have, _) => 
						println("overbudget,");
						outcome = _makeOverBudgetOutcome(need,have);
				}
				return outcome
			}
		}

		/** internal method used by server, submits a Multi-estimate Task task to Automan
		*
		*  @param task - submitted task
		*  @param adptr - adapter with credentials to connect to the crowdsource back-end
		*  @return a new MultiestimateOutcome, representing the outcome of the task. 
		*							
		*/
		def multiestimateTask(task : Task, adptr: AdapterCredentials) : MultiestimateOutcome = {
			println("ERROR: MULTIESTIMATE NOT IMPLEMENTED");
			return MultiestimateOutcome()
		}

		/** internal method used by server, submits a Radio task to Automan
		*
		*  @param task - submitted task
		*  @param adptr - adapter with credentials to connect to the crowdsource back-end
		*  @return a new RadioOutcome, representing the outcome of the task. 
		*							
		*/
		def radioTask(task : Task, adptr: AdapterCredentials) : RadioOutcome = {
			println("ERROR: RADIO NOT IMPLEMENTED");
			return RadioOutcome()
		}

		/** internal method used by server, submits a radio distribution task to Automan
		*
		*  @param task - submitted task
		*  @param adptr - adapter with credentials to connect to the crowdsource back-end
		*  @return a new RadioDistOutomce, representing the outcome of the task. 
		*							
		*/
		def radioDistTask(task : Task, adptr: AdapterCredentials) : RadioDistOutcome = {
			println("ERROR: RADIO DIST NOT IMPLEMENTED");
			return RadioDistOutcome()
		}

		/** internal method used by server, submits a checkbox task to Automan
		*
		*  @param task - submitted task
		*  @param adptr - adapter with credentials to connect to the crowdsource back-end
		*  @return a new CheckboxOutcome, representing the outcome of the task. 
		*							
		*/
		def checkboxTask(task : Task, adptr: AdapterCredentials) : CheckboxOutcome = {
			println("ERROR: CHECKBOX NOT IMPLEMENTED");
			return CheckboxOutcome()
		}

		/** internal method used by server, submits a checkbox dist task to Automan
		*
		*  @param task - submitted task
		*  @param adptr - adapter with credentials to connect to the crowdsource back-end
		*  @return a new CheckboxDistOutcome, representing the outcome of the task. 
		*							
		*/
		def checkboxDistTask(task : Task, adptr: AdapterCredentials) : CheckboxDistOutcome = {
			println("ERROR: CHECKBOX DIST NOT IMPLEMENTED");
			return CheckboxDistOutcome()
		}

		/** internal method used by server, submits a freetext task to Automan
		*
		*  @param task - submitted task
		*  @param adptr - adapter with credentials to connect to the crowdsource back-end
		*  @return a new FreetextOutcome, representing the outcome of the task. 
		*							
		*/
		def freetextTask(task : Task, adptr: AdapterCredentials) : FreetextOutcome = {
			println("ERROR: FREETEXT NOT IMPLEMENTED");
			return FreetextOutcome()
		}

		/** internal method used by server, submits a freetext dist task to Automan
		*
		*  @param task - submitted task
		*  @param adptr - adapter with credentials to connect to the crowdsource back-end
		*  @return a new FreetextDistOutcome, representing the outcome of the task. 
		*							
		*/
		def freetextDistTask(task : Task, adptr: AdapterCredentials) : FreetextDistOutcome = {
			println("ERROR: FREETEXT DIST NOT IMPLEMENTED");
			return FreetextDistOutcome()
		}


		/** Report the status of the server
		*
		*  @return a new ServerStatusResponse, representing the state of the server. Either Running or Killed
		*							
		*/
		def serverStatus(e: Empty) : Future[ServerStatusResponse] = {
			var ssr = ServerStatusResponse();
			if (self.running()){
				ssr.withReturnCode(ServerStatusResponse.StatReturnCode.RUNNING)
			}else{
				ssr.withReturnCode(ServerStatusResponse.StatReturnCode.KILLED)
			}
			Future.successful(ssr);
		}

		/** Register a crowdsource back-end adapter to the server.
		*
		*  @param adptr - adapter with credentials to connect to the crowdsource back-end
		*  @return a new RegistrationResponse, representing the whether the adapter was registered successfully or not
		*							
		*/
		def registerAdapter(adptr : AdapterCredentials) : Future[RegistrationResponse] = {
			// add error checking
			_adptr_credentials = Some(adptr);
			Future.successful(RegistrationResponse().withReturnCode(RegistrationResponse.RegReturnCode.OKAY));
		}

		/** Shutdown the gRPC server
		*
		*  @return a new ServerStatusResponse, representing the state of the server. Either Running or Killed
		*							
		*/
		def killServer(e: Empty) : Future[ServerStatusResponse] = {
			println("Server Shutting Down..")
			self.stop_server();
			Future.successful(ServerStatusResponse().withReturnCode(ServerStatusResponse.StatReturnCode.KILLED));
		}

	}

	def main(args: Array[String]) : Unit = {
		// add argument parsing
		var localport = 50051;
		if(args.length >1) localport = args(0).toInt;

		val ssdef = EstimationPrototypeGrpc.bindService(new EstimationServicer(), ExecutionContext.global)
		println("Server Started on port "+localport+" ...")
		runServer(ssd = ssdef, port = localport)
	}
}