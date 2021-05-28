__author__ = 'Bucky'
__author__ = 'Bucky'
import paramiko
import threading
import json

# connect函数中，参数是一个主机的IP地址或者是主机名称，
# 在执行这个方法之后，如果成功的连接到服务器，那么就会返回一个sshclient对象
def connect(host):
    # 建立一个SSHClient的对象
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,22,username="root",password="123456")
        return ssh
    except:
        return None

# 定义命令，在参数中，一个是args，一个outpath，args表示命令的参数，而outpath表示为可执行文件的路径
def command(args,outpath):
    cmd='%s %s'%(outpath,args)
    return cmd

# 执行命令，传入的参数一个为连接的对象conn，一个为需要执行的命令cmd
def exec_commands(conn,cmd):
    stdin,stdout,stderr=conn.exec_command(cmd)
    result=stdout.read()
    return result

# 上传文件，传入已连接对象conn,上传文件，上传文件地址+文件名
def upload_file(conn,upflie,outpath):
    ftp=conn.open_sftp()
    ftp.put(upflie,outpath)
    ftp.close()
    return "上传成功，地址： "+outpath

# 下载文件，传入已连接对象conn,下载文件，下载文件地址+文件名
def download_files(conn,downfile,outpath):
    ftp=conn.open_sftp()
    ftp.get(downfile,outpath)
    ftp.close()
    return "下载成功，地址： "+outpath

# 整合以上linux连接--命令执行
def excutor(host,outpath,args):
    conn=connect(host)
    if not conn:
        return [host,None]
    cmd=command(args,outpath)
    result=exec_commands(conn,cmd)
    result = json.dumps(result.decode(encoding="utf-8"),indent=4,ensure_ascii=False)
    return [host, result]