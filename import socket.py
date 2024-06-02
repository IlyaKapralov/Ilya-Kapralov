import socket

server = socket.socket()

server.bind(('localhost', 3000))

server.listen(5)
print('server', server)

con, addr = server.accept()
print('connection ', con)
print('client addr ', addr)

con.close()
server.close()