from __future__ import print_function
import grpc
import rss_pb2
import rss_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = rss_pb2_grpc.RssServiceStub(channel)
    response = stub.Reply(rss_pb2.ReplyRequest(message='hoge'))
    print("Client received: " + response.message)

    response = stub.Inspect(rss_pb2.InspectRequest(uri='http://www.fujlog.net'))
    print("Client received: " + str(response.rss))


if __name__ == '__main__':
    run()
