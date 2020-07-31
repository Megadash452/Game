import socket
from _thread import *
import sys

server = "192.168.1.9"
port = 5551

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


def read_pos(string):
    string = string.split(",")
    return int(string[0]), int(string[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]


def threaded_client(connection, player):
    connection.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(connection.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                #print("Received: ", data)
                #print("Sending : ", reply)

            connection.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    connection.close()


current_player = 0
while True:
    connection, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (connection, current_player))
    current_player += 1
