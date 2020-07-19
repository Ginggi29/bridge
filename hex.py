from XOR_CheckSum import *
import serial
import sys
import socket



HOST = '172.20.10.7'  
PORT = 6666       
#ser = serial.Serial('COM5', 115200)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        #print('received', repr(data.decode('utf-8')))
        #print('Converted to Hex', data.decode('hex'))
        datasock = data.hex()
        print('Converted to Hex : ', datasock)

ser = serial.Serial('COM7', 115200)
#print sys.argv[1]

 
#cek saldo 100204 3030303031310000 00 1003
header = bytes.fromhex('100201')
#body = bytes.fromhex('303030303131002A323334353630303030303030303030303030303330303030353030303235303932303138313631353032')
body = bytes.fromhex(datasock)
footer = bytes.fromhex('1003')
r = hex(xor_checksum_string(body))
o = bytes.fromhex(r[2:])

hasil = str(header.decode())+ str(body.decode()) + str(o.decode()) + str(footer.decode())
print (hasil)
print()
y = (hasil.encode('utf-8').hex())
print (y)
ser.write(hasil.encode())
