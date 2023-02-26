import socket

s = socket.socket()
host = '172.20.4.215'
port = 8080
s.bind((host, port))
print("")
print("server is currently running @ ", host)
print("")
print("waiting for ...if there is any connection up")

s.listen(1)

print("")

conn, addr = s.accept()

print(addr, "has been successfully connected to the server")

print("")
command = input(str("command>> "))
if command == "pwd":
    conn.send(command.encode())
    print("")
    print("command has been send successfully ")
    print("")

    files = conn.recv(5000)
    files = files.decode()
    print("command output : ", files)
else:
    print("")
    print("OPPPPPPSSSSS SORRY : command not recongnized : ")

filename = input(str("please enter the textfile name : "))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("textfile has been send successfully :) ")
