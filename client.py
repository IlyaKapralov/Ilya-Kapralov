import socket

client = socket.socket()

client.connect(('localhost', 3000))

data = client.recv(1024)
print('Сообщение в бинарном виде', data)
print('Входящее сообщение', data.decode())

message = 'Привет сервер!'
data = message.encode()
client.send(data)

def getMessages():
    while True:
        data = con.recv(1024)
        print('Входящее сообщение', data.decode())
        if data.decode() =='Закрывай!':
            break
    client.close()

start_new_thread(getMessages, ())


while True:
    message = input('Введите сообщение')
    data = message.encode()
    client.send(data)
    if message == 'Закрывай':
    #print('Сообщение в бинарном виде', data)
    #print('Входящее сообщение', data.decode())
    #if data.decode() =='Закрывай!':
        break


client.close()