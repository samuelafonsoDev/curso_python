
""""
iscompleted = True
users = "Samuel"
print(iscompleted)
x = 2
y =4
if(x is not y):
    print(f"x={x} é diferente de y{y}")
else:
    print("São igual")
print("---------fim-----")

contador = 0
for itervar in [3, 41, 12, 9, 74, 15,3]:
    contador = contador + 1
print('Contagem:' , contador)

"""
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org, 80'))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='' )
mysock.close()