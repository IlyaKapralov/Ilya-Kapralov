import socket
from _thread import start_new_thread

server = socket.socket()

server.bind(('192.168.51.238', 3000))

server.listen(5)
print('server', server)

con, addr = server.accept()
message = 'Привет клиент!'
data = message.encode()
con.send(data)
#бесконечный цикл получения сообщений
def getMessages():
    while True:
        data = con.recv(1024)
        print('Входящее сообщение', data.decode())
        if data.decode() =='Закрывай!':
            break
    con.close()
    server.close()

start_new_thread(getMessages,())

while True:
   message = input('Введите сообщение: ')
   data = message.encode()
   con.send(data)
   if message == 'Закрывай!':
       break
#con, addr = server.accept()
#message = 'Привет клиент!'
#data = message.encode()
#con.send(data)
#print('connection ', con)
#print('client addr ', addr)

#data = con.recv(1024)
#print('Сообщение в бинарном виде', data)
#print('Входящее сообщение', data.decode())
con.close()
server.close()