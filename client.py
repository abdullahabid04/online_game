# create directory(client)

import os
import socket

s = socket.socket()
host = '172.20.4.215'
port = 8080

host = input(str("enter the host address : "))
print("")

s.connect((host, port))
print("connected to the server successfully ")
print("")
print("")

command = s.recv(1024)
command = command.decode()
print("command recieved")
print("")
if command == "pwd":
    files = os.getcwd()
    files = str(files)

    s.send(files.encode())
    print("command is executed successfuly. . .")

else:
    print("")
    print("OPPPPPPSSSSS SORRY : command not recongnized : ")

filename = input(str("enter the textfile name : "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()

print("file has been recieved successfully")
