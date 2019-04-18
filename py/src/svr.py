from concurrent import futures
import time

import grpc

from rss_pb2 import ReplyResponse, InspectResponse
from rss_pb2_grpc import RssServiceServicer
from rss_pb2_grpc import add_RssServiceServicer_to_server

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class RssServicer(RssServiceServicer):
    def Reply(self, request, context):
        print('reply!')
        return ReplyResponse(message='ほげ')

    def Inspect(self, request, context):
        print('inspect!')
        return InspectResponse(rss=['hoge', 'ika'])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_RssServiceServicer_to_server(
            RssServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()