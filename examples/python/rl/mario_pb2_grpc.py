# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import mario_pb2 as mario__pb2


class GRPCMarioStub(object):
  """`service` is used to define methods for gRPC services in a fixed format, similar to defining
  an interface in Golang
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAction = channel.unary_unary(
        '/mario.GRPCMario/GetAction',
        request_serializer=mario__pb2.Request.SerializeToString,
        response_deserializer=mario__pb2.Response.FromString,
        )


class GRPCMarioServicer(object):
  """`service` is used to define methods for gRPC services in a fixed format, similar to defining
  an interface in Golang
  """

  def GetAction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GRPCMarioServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAction': grpc.unary_unary_rpc_method_handler(
          servicer.GetAction,
          request_deserializer=mario__pb2.Request.FromString,
          response_serializer=mario__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mario.GRPCMario', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))