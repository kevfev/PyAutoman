import core.automanlib as pyAutomanlib
from core.automanlib_rpc_pb2 import TaskResponse
import random
import sys

class Automan():
	"""
	The Automan Class.

    Attributes
    ----------
    adptr : dict
        A dictionary containing the parameters for the adapter
    srvr_addr : str
    	The hostname for the gRPC server
    port : int 
    	The port to connect to on the hostname 
    channel: Channel
    	The gRPC channel to communicate over

    """

	def __init__(self, adapter, server_addr = 'localhost', port = 50051):
		"""
		Ensure necessary fields in adapter are initializated and
		set up the gRPC channel

        Parameters
        ----------
        adapter : dict
            A dictionary containing the parameters for the adapter
	    server_addr : str
	    	The hostname for the gRPC server
	    port : int 
	    	The port to connect to on the hostname 

        """
		self.adptr = pyAutomanlib.make_adapter(adapter["access_id"], adapter["access_key"], sandbox_mode=adapter["sandbox_mode"]) if pyAutomanlib.isGoodAadapter(adapter) else None
		self.srvr_addr = server_addr
		self.port = port
		self.channel = self.init_channel(server_addr, port)

		if self.adptr is None:
			sys.exit("Invalid adapter, check parameters used")

		# set up channel, connect to gRPC server, register adapter credentials with server
		self.stub = self.init_channel(server_addr, port)
		pyAutomanlib.register_adapter_to_server(self.channel, self.adptr)

	def _handleResponse(self,response):
		"""
		Internal method. Parse the response from the gRPC server. First determine if response is valid.
		The field return_code can take the following values:
			TaskResponse.VALID 
			TaskResponse.ERROR
			TaskResponse.EXCEPTION

        Parameters
        ----------
        response : TaskResponse
            The response from the server

        Returns
        -------
        TaskOutcome
        	If the response is valid, it returns the outcome of the task
        None
            If there was an error or exception, the function terminates the script and prints an error message to output

        """
		ret_string = None
		if response.return_code == TaskResponse.VALID:
			return response.outcome
		if response.return_code == TaskResponse.UNDEFINED_RESP_CODE:
			ret_string= "ERROR: An undefind response code was returned. Application may be out of data or there is an error on the grpc server side"
		if response.return_code == TaskResponse.ERROR:
			ret_string = "ERROR: An error occured \n"+ "Message: "+response.err_msg
		if response.return_code == TaskResponse.EXCEPTION:
			ret_string ="EXCEPTION: An exception occured \n"+ "Message: "+response.excep_msg

		sys.exit(ret_string)

	def _shutdown(self):
		"""
		Internal method. Shutdown the gRPC server

        """
		pyAutomanlib.shutdown_rpc_server(self.channel)

	def _init_channel(self, server_addr, port):
		"""
		Internal method. Create the gRPC channel

		Parameters
        ----------
	    server_addr : str
	    	The hostname for the gRPC server
	    port : int 
	    	The port to connect to on the hostname 

        Returns
        -------
        Channel
            A channel that connects to the gRPC back-end server

        """
		self.channel = pyAutomanlib.make_channel(server_addr,str(port))

	def estimate(self, text, budget, title, image_url):
		"""
		Estimates the answer to the provided task. Calls AutoMan's estimate functionality on the back-end

		Parameters
        ----------
		title_ : str
			The title for the task, to display to workers on the crowdsource platform
		text_ : str
			The text description of the task, to display to workers on the crowdsource platform
		image_url_ : str
			The url of the image for the task
		budget_ : double
			The total budget allocated for this task


        Returns
        -------
        TaskOutcome
            The outcome of the estimation. Can be either a:
            Estimate - indicates estimation was successful
			LowConfidenceEstimate - indicates low confidence estimate
			OverBudgetEstimate - indicates estimation attempt went over budget

			given by enum types:
			TaskOutcome.OutcomeType.ESTIMATE
			TaskOutcome.OutcomeType.LOW_CONFIDENCE_EST
			TaskOutcome.OutcomeType.OVER_BUDGET_EST

        """
		task = pyAutomanlib.make_est_task(text_ = text,
	    								budget_ = budget,
	    								title_ = title,
	    								image_url_ = "https://docs.google.com/uc?id=1ZQ-oL8qFt2tx_T_-thev2O4dsugVbKI2")
		resp = pyAutomanlib.submit_task(self.channel, task)
		outcome = self.handleResponse(resp)

		return outcome