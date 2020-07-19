import socket
import sys

result1 = sys.argv[1]


results1 = bytes(result1, encoding= 'utf-8')


HOST = '192.168.43.241'
PORT = 6666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
   # data = 'result'
    s.sendall(results1)
    s.close()
print(result)
            

