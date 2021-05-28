__author__ = 'Bucky'
from pymongo import MongoClient
import paramiko
import threading
import os


#清除Mongodb数据
  ##注意：需要在mongod.conf文件中加入 bind_ip = 0.0.0.0
  ##绑定运行访问ip。0.0.0.0允许所有ip访问。
def cleanMongo(ip):
        con=MongoClient(ip,27017)
        db=con['named-objects']
        drop=db.command("dropDatabase") #清除整个named-objects库
        print(drop)
        return "清除Mongodb数据：成功  "




#清除ood上cyfs的旧数据
def cleanCyfs(ssh):
    #定义删除cyfs目录及进程命令
    cleanExe=['sudo kill -9 $(pidof gateway)',
              'sudo kill -9 $(pidof im-service)',
              'sudo kill -9 $(pidof file-manager)',
              'sudo kill -9 $(pidof chunk-manager)',
              'sudo kill -9 $(pidof app-manager)',
              'sudo kill -9 $(pidof ood-daemon)',
              'rm -r /cyfs']
    try:
        #运行命令
        for exe in cleanExe:
            stdin1,stdout1,stderr1=ssh.exec_command(exe)
        return "清除ood数据：成功"
    except:
        return "清除ood数据：失败"

if __name__=="__main__":
        #检查并运行代码
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(hostname='192.168.100.132',port=22,username='root',password='123456')
        print(cleanMongo("192.168.100.132"))
        print(cleanCyfs(ssh))



