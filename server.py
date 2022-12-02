# server.py //文件名
import socket #导入socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建socket
server.bind(('10.0.0.1', 44444)) #绑定IP/端口
server.listen(5) #监听
print('starting....')
conn, addr = server.accept() #连接
print(conn)
print('client addr', addr)
print('ready to recv the passwd...')
client_msg = conn.recv(1024)
print('client passwd changed: %s' % client_msg)
conn.send(client_msg.upper())
conn.close()
server.close()