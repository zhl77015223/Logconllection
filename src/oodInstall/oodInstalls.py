__author__ = 'Bucky'
import paramiko
import os
from time import sleep

#上传文件
def upload_file(conn,upflie,outpath):
    ftp=conn.open_sftp()
    ftp.put(upflie,outpath)
    ftp.close()
    return "上传成功，地址： "+outpath

#配置ood环境
def creatOod(ssh):
    #定义创建目录命令
    creatdir=[
        'mkdir /cyfs',
        'mkdir /cyfs/etc',
        'mkdir /cyfs/etc/desc',
        'cp /ood/app_repo.desc  /cyfs/etc/desc',
        'cp /ood/cyfs_repo.desc  /cyfs/etc/desc'
    ]
    #执行创建目录命令
    try:
        for exe in creatdir:
            stdin1,stdout1,stderr1=ssh.exec_command(exe)
            sleep(2)
        return '配置ood环境:成功'
    except:
        return '配置ood环境:失败'

#安装ood
def oodinstall(ssh,toolPath):
    upload_file(ssh,toolPath,'/ood/ood-installer',)
    sleep(2)
    try:
        #执行创建目录命令
        stdin11,stdout11,stderr11=ssh.exec_command('chmod +x /ood/ood-installer')
        sleep(2)
        stdin22,stdout22,stderr22=ssh.exec_command('sudo /ood/ood-installer --no-cyfs-repo --no-app-repo')
        sleep(10)
        return  '安装OOD:成功'
    except:
        return '安装OOD:失败'



#修改日志debug级别
def modificationLevel(ssh,toolPath):
    try:
        #执行命令
        upload_file(ssh,toolPath,'/cyfs/etc/debug.cfg')
        stdin11,stdout11,stderr11=ssh.exec_command('ps -ef | grep -E "gateway|file-manager|chunk-manager|app-manager|im-service|ood-daemon"')
        return '修改日志debug级别:成功\n'+stdout11.read().decode()

    except:
        return '修改日志debug级别:失败'


#查看版本号
def version(ssh):
    exes=[
        'objdump -s -j versection /cyfs/app/9tGpLNnfbRQD28vw69SF8jri6Mhwq6Xqd6FfinCfbvBL/im-service',
        'objdump -s -j versection /cyfs/services/gateway/current/bin/gateway'
    ]
    try:
        #执行命令
        for exe in exes:
            stdin1,stdout1,stderr1=ssh.exec_command(exe)
            return stdout1.read()
    except:
        return "查看版本号失败"

if __name__=="__main__":
        #检查并运行代码
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(hostname='192.168.100.147',port=22,username='root',password='123456')
        #执行配置repo命令
        print(creatOod(ssh))
        #执行ood安装命令
        oodInstallPath='tool\\ood-installer'
        print(oodinstall(ssh,oodInstallPath))
        # #执行修改日志级别命令
        modificationLevelPath='tool\\debug.cfg'
        print(modificationLevel(ssh,modificationLevelPath))