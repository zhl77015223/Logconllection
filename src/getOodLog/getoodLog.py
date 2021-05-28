import paramiko
import threading
import os

# 使用工具前:
#     （1）需要先在保存日志的路径下放一个log.tar.gz，便于下载文件；
#     （2）修改服务器ip地址

# 利用线程一次对多个服务器操作
class MyThread(threading.Thread):
    def __init__(self,host,user="root",pwd="123456",port=22):
        self.host=host
        self.user=user
        self.pwd=pwd
        self.port=port
        super().__init__()

    def run(self):
        # 创建客户端
        ssh=paramiko.SSHClient()
        # 设置白名单不提醒
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

        # 连接
        ssh.connect(hostname=self.host,port=self.port,username=self.user,password=self.pwd)

        # 对日志进行打包处理
        stdin1,stdout1,stderr1=ssh.exec_command('tar -zcvf /ood/log.tar.gz /cyfs/log/')
        print(stdout1.read().decode())

        # 下载日志
        ftp=ssh.open_sftp()
        savelog="log\\"          #下载日志路径,使用前需修改
        saveflielog=savelog+self.host+"log.tar.gz"
        ftp.get("/ood/log.tar.gz",saveflielog)
        ftp.close()
        print("下载成功,host: "+self.host)

        # 清除linux已下载日志
        stdin2,stdout2,stderr2=ssh.exec_command('rm -r /ood/log.tar.gz')
        print(stdout2.read().decode())

        # 关闭连接
        ssh.close()
if __name__ == '__main__':
    savelog="log\\"                                   #下载日志路径
    data=[                                             #服务器信息，使用前需修改
        # {'host': '192.168.100.147'},
        # {'host':'192.168.100.130'},
        {'host': '192.168.100.131'},
        {'host': '192.168.100.132'},
        # {'host': '192.168.100.138'},

    ]
    tlist=[]
    for x in data:
        copyfile="copy "+savelog+"log.tar.gz "+savelog+x['host']+"log.tar.gz"
        text=os.system(copyfile)
        t=MyThread(host=x['host'])
        tlist.append(t)

    for x in tlist:
        x.start()