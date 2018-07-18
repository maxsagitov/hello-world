import socket, string, serial
ser = serial.Serial('/dev/ttyACM0', 9600)
 
HOST = "192.168.0.111"                 # localhost 
PORT = 33333 
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
srv.bind((HOST, PORT))
while 1: 
  print ('Слушаю порт 33333') 
  srv.listen(1)              
  sock, addr = srv.accept() 
  while 1:
    try:
      pal = sock.recv(2)
    except Exception:
      break
    
    if not pal:  
      break 
    print ("Получено от %s:%s:" % addr, pal)
    ser.write (pal)
    s=str(ser.readline())
    print ("Отправлено %s:%s:" % addr, s)
    try:
      data = (bytes(s, encoding='ascii'))
      sock.send(data)
    except Exception:
      break 

