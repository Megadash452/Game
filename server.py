import socket
from _thread import *
import sys

server = ''
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print('Waiting for connection. Server Started.')


def threaded_client(connection):
    connection.send(str.encode('Connected'))

    reply = ''
    while True:
        try:
            data = connection.receive(2048)
            reply = data.decode('utf-8')

            if not data:
                print('Disconnected')
                break
            else:
                print('Received: ', reply)
                print('Sending: ', reply)

            connection.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    connection.close()


while True:
    connection, addr = s.accept()
    print('Connected to: ', addr)

    start_new_thread(threaded_client, (connection, ))
