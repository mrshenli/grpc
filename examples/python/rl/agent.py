# Copyright 2019 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The example of four ways of data transmission using gRPC in Python."""

from threading import Thread
from concurrent import futures

import grpc
import mario_pb2_grpc
import mario_pb2
import pickle
import torch

__all__ = 'MarioServer'
SERVER_ADDRESS = 'localhost:23333'
SERVER_ID = 1


class MarioAgent(mario_pb2_grpc.GRPCMarioServicer):

    # 一元模式(在一次调用中, 客户端只能向服务器传输一次请求数据, 服务器也只能返回一次响应)
    # unary-unary(In a single call, the client can only send request once, and the server can
    # only respond once.)
    def GetAction(self, request, context):

        py_request = pickle.loads(request.request_data)
        py_response = list(py_request)
        py_response[2] += 1
        print(f"server got {py_request}")
        response = mario_pb2.Response(
            server_id=SERVER_ID,
            response_data=pickle.dumps(py_response))
        return response


def main():
    server = grpc.server(futures.ThreadPoolExecutor())

    mario_pb2_grpc.add_GRPCMarioServicer_to_server(MarioAgent(), server)

    server.add_insecure_port(SERVER_ADDRESS)
    print("------------------start Python GRPC server")
    server.start()
    server.wait_for_termination()

    # If raise Error:
    #   AttributeError: '_Server' object has no attribute 'wait_for_termination'
    # You can use the following code instead:
    # import time
    # while 1:
    #     time.sleep(10)


if __name__ == '__main__':
    main()
