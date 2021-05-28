__author__ = 'Bucky'
import os
import time
#安装app
def appinstall(devicesid):
    for id in devicesid:
        #读取安装包
        apppath=os.listdir("app")
        #执行安装命令
        for app in apppath:
            appinstall="adb -s "+id+" install app/"+app
            text=os.system(appinstall)
        time.sleep(2)
        print(text)
def main():
    #设置设备的id
    devicesid={
        "2db7169f":"A",
        # "14277172":"D",
        # "6740108":"C",
        "TGBQZTIF6XPZGACA":"B",
        #  "70f58ecf":"my"
        }
    # 安装app
    appinstall(devicesid)

if __name__ == '__main__':
     main()