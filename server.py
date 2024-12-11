from concurrent import futures
import grpc
import hello_pb2
import hello_pb2_grpc

class HelloService(hello_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        response = hello_pb2.HelloResponse()
        response.message = f"Hola, {request.name}!"
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    print("Servidor RPC en funcionamiento...")
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
