import socket, sys
 
HOST = "46.188.74.18"        # удаленный компьютер (localhost) 
PORT = 33333              # порт на удаленном компьютере 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.connect((HOST, PORT))
while 1:
    datav = input()
    if datav is "q":
        sock.close()
        sys.exit()
    data = (bytes(datav, encoding='ascii'))
    sock.send(data) 
    result = sock.recv(1024)
    print ("Получено:", result) 


