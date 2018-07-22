# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import automanlib_classes_pb2 as automanlib__classes__pb2
import automanlib_rpc_pb2 as automanlib__rpc__pb2


class EstimationPrototypeStub(object):
  """****
  This .proto file defins the rpc service and the messages sent
  and received by the various rpc method calls. 
  ***

  ****
  This service is a prototype of the Estimation functionality of
  AutoMan only. 
  RPC methods:

  KillServer 
  This method shuts the rpc server down
  parameters:
  None
  returns:
  ServerStatusResponse
  Indicates the current status of the server, "KILLED" if the
  method was successful

  RegisterAdapter 
  Registers a crowdsource back-end for the AutoMan server to use for
  authentication
  parameters:
  AdapterCredentials 
  returns:
  RegistrationResponse
  Indicates if the credentials were registered successfully or not


  ServerStatus 
  Reports the status of the server
  parameters:
  None 
  returns:
  ServerStatusResponse
  Indicates the current status of the server, either "RUNNING" or 
  "KILLED"


  SubmitTask 
  Submits a task to the AutoMan server to post to the crowdsource back-end
  parameters:
  AutomanTask 
  returns:
  TaskResponse
  A response from the Automan server on the submitted task
  If the response code is VALID, the 
  task was completed successfully and one of task_outcome will be set depending
  on the respective task.
  If the response code was ERROR, an error occured and the err_code and err_msg
  fields will be set.
  If the response code was EXCEPTION, an exception occured and the excep_code
  and excep_msg fields will be set.

  ***
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.KillServer = channel.unary_unary(
        '/EstimationPrototype/KillServer',
        request_serializer=automanlib__rpc__pb2.Empty.SerializeToString,
        response_deserializer=automanlib__rpc__pb2.ServerStatusResponse.FromString,
        )
    self.RegisterAdapter = channel.unary_unary(
        '/EstimationPrototype/RegisterAdapter',
        request_serializer=automanlib__classes__pb2.AdapterCredentials.SerializeToString,
        response_deserializer=automanlib__rpc__pb2.RegistrationResponse.FromString,
        )
    self.SubmitTask = channel.unary_unary(
        '/EstimationPrototype/SubmitTask',
        request_serializer=automanlib__rpc__pb2.AutomanTask.SerializeToString,
        response_deserializer=automanlib__rpc__pb2.TaskResponse.FromString,
        )
    self.ServerStatus = channel.unary_unary(
        '/EstimationPrototype/ServerStatus',
        request_serializer=automanlib__rpc__pb2.Empty.SerializeToString,
        response_deserializer=automanlib__rpc__pb2.ServerStatusResponse.FromString,
        )


class EstimationPrototypeServicer(object):
  """****
  This .proto file defins the rpc service and the messages sent
  and received by the various rpc method calls. 
  ***

  ****
  This service is a prototype of the Estimation functionality of
  AutoMan only. 
  RPC methods:

  KillServer 
  This method shuts the rpc server down
  parameters:
  None
  returns:
  ServerStatusResponse
  Indicates the current status of the server, "KILLED" if the
  method was successful

  RegisterAdapter 
  Registers a crowdsource back-end for the AutoMan server to use for
  authentication
  parameters:
  AdapterCredentials 
  returns:
  RegistrationResponse
  Indicates if the credentials were registered successfully or not


  ServerStatus 
  Reports the status of the server
  parameters:
  None 
  returns:
  ServerStatusResponse
  Indicates the current status of the server, either "RUNNING" or 
  "KILLED"


  SubmitTask 
  Submits a task to the AutoMan server to post to the crowdsource back-end
  parameters:
  AutomanTask 
  returns:
  TaskResponse
  A response from the Automan server on the submitted task
  If the response code is VALID, the 
  task was completed successfully and one of task_outcome will be set depending
  on the respective task.
  If the response code was ERROR, an error occured and the err_code and err_msg
  fields will be set.
  If the response code was EXCEPTION, an exception occured and the excep_code
  and excep_msg fields will be set.

  ***
  """

  def KillServer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisterAdapter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubmitTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ServerStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EstimationPrototypeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'KillServer': grpc.unary_unary_rpc_method_handler(
          servicer.KillServer,
          request_deserializer=automanlib__rpc__pb2.Empty.FromString,
          response_serializer=automanlib__rpc__pb2.ServerStatusResponse.SerializeToString,
      ),
      'RegisterAdapter': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterAdapter,
          request_deserializer=automanlib__classes__pb2.AdapterCredentials.FromString,
          response_serializer=automanlib__rpc__pb2.RegistrationResponse.SerializeToString,
      ),
      'SubmitTask': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitTask,
          request_deserializer=automanlib__rpc__pb2.AutomanTask.FromString,
          response_serializer=automanlib__rpc__pb2.TaskResponse.SerializeToString,
      ),
      'ServerStatus': grpc.unary_unary_rpc_method_handler(
          servicer.ServerStatus,
          request_deserializer=automanlib__rpc__pb2.Empty.FromString,
          response_serializer=automanlib__rpc__pb2.ServerStatusResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'EstimationPrototype', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
