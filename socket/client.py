from rpc import RPCClient
server = RPCClient('localhost', 8088)
server.connect()
print(server.add(5, 6))
print(server.sub(5, 6))
print(server.hi())
print(server.multi(5, 6))
server.disconnect()