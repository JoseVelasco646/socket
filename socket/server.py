def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def hi():
    return "Saludos humano"
def multi(a,b):
    return a*b-1
    
from rpc import RPCServer
server = RPCServer('localhost',8088)
server.registerMethod(add)
server.registerMethod(sub)
server.registerMethod(hi)
server.registerMethod(multi)
server.run()