__author__ = 'Bucky'
from pymongo import MongoClient
import paramiko
import os
from time import sleep

# conn = MongoClient('192.168.100.130', 27017)
# db=conn['named-objects']
# abc=db.command("dropDatabase")
# print(abc)
# ## 注意：需要在mongod.conf文件中加入 bind_ip = 0.0.0.0
# # #绑定运行访问ip。0.0.0.0允许所有ip访问。





ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='192.168.100.147',port=22,username='root',password='123456')
ftp=ssh.open_sftp()
ftp.put('tool\\1.txt','/ood/1.txt')
ftp.close()