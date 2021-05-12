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

import time
import grpc
import pickle
import torch

import mario_pb2_grpc
import mario_pb2

__all__ = [
    'simple_method',
]

SERVER_ADDRESS = "localhost:23333"
CLIENT_ID = 1

# 中文注释和英文翻译
# Note that this example was contributed by an external user using Chinese comments.
# In all cases, the Chinese comment text is translated to English just below it.


# 一元模式(在一次调用中, 客户端只能向服务器传输一次请求数据, 服务器也只能返回一次响应)
# unary-unary(In a single call, the client can only send request once, and the server can
# only respond once.)
def get_action(stub, *args):
    pickle.dumps(args)
    request = mario_pb2.Request(client_id=CLIENT_ID,
                               request_data=pickle.dumps(args))
    response = stub.GetAction(request)
    print(f"resp is {pickle.loads(response.response_data)}")
    print("--------------Call SimpleMethod Over---------------")



def main():
    with grpc.insecure_channel(SERVER_ADDRESS) as channel:
        stub = mario_pb2_grpc.GRPCMarioStub(channel)
        get_action(stub, 7, torch.zeros(2, 2), torch.ones(3, 3))


if __name__ == '__main__':
    main()
