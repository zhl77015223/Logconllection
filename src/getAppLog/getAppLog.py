__author__ = 'Bucky'
import os
import time


#获取日志及截图
def getAppLog(devicesid,savelog):
    #定义adb日志获取,adb 截图命令
    for id in devicesid:

        #获取超送的peopleid
        appexe1=os.popen("adb -s "+id+" shell \"ls /sdcard/Android/data/io.cyim/files/\"")
        time.sleep(1)
        people_id=appexe1.read()[0:44]
        print(people_id)

        #定义保存日志的路径
        savelog1=savelog+devicesid[id]+"log"
        print(savelog1)

        #创建保存日志的文件
        os.system("mkdir "+savelog1)

        #定义执行日志获取命令
        appLog="adb -s "+id+" pull /sdcard/Android/data/io.cyim/files/log/  "+savelog1
        imclientLog="adb -s "+id+" pull /sdcard/Android/data/io.cyim/files/"+people_id+"/log/imclient/ "+savelog1
        #定义截屏命令
        screenshot="adb -s "+id+" shell /system/bin/screencap -p /sdcard/screenshot.png"
        getscreenshot="adb -s "+id+" pull /sdcard/screenshot.png "+savelog1

        #执行命令
        appexe2=os.system(imclientLog)
        appexe3=os.system(appLog)
        appexe4=os.system(screenshot)
        appexe5=os.system(getscreenshot)

def main():
    #设置设备的id
    devicesid={
        "2db7169f":"A-147",
        # "TGBQZTIF6XPZGACA":"B-130",
        # "14277172":"D-132",
        # "6740108":"C-138",
        # "70f58ecf":"my"
        }
    #设置日志保存路径，需要对应上面的进行创建
    savelog="log\\" #注意：保存的路径不要有中文字符，会报错
    getAppLog(devicesid,savelog)

if __name__ == '__main__':
     main()