__author__ = 'Bucky'
import paramiko
import threading
import os
from oodInstall.oodclean import cleanCyfs,cleanMongo
from oodInstall.oodInstalls import upload_file,creatOod,oodinstall,modificationLevel
from time import sleep
#使用指示
#1.mongod.cfg配置中需添加bind_ip:0.0.0.0
#2.首次使用需将tool下的进程 放置在创建好/ood下

def run(host):
    # 创建客户端
    ssh=paramiko.SSHClient()
    # 设置白名单不提醒
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    # 连接
    ssh.connect(hostname=host,port=22,username="root",password="123456")

    #清除所有cyfs旧数据
    print(host+': 清除旧数据中...')
    print(cleanMongo(host))
    print(cleanCyfs(ssh))

    #安装ood
    print(host+': 安装ood中...')
    print(creatOod(ssh))
    oodInstallPath='tool\\ood-installer'
    print(oodinstall(ssh,oodInstallPath))
    modificationLevelPath='tool\\debug.cfg'
    print(modificationLevel(ssh,modificationLevelPath))

    # 关闭连接
    ssh.close()
if __name__ == '__main__':
    hosts={
        # 'host0':'192.168.100.130',
        # 'host1': '192.168.100.131',
        'host2': '192.168.100.138',
        # 'host3': '192.168.100.136',
        # 'host4': '192.168.100.147',
        }
    for h in hosts:
        run(hosts[h])





