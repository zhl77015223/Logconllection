__author__ = 'Bucky'
import re
from datetime import  datetime
import xlwt
# # 该message仅作为举例
# i = '###### 5r4MYfFes7ean6WqitqNeBppstmmGvntgVo4hYfrHvUa recv msg. from:5bnZHzYCu7fubhsG3KpG9ThQTSS5g2AtbbJPCyRCn7Ha, owner:5r4MYfFZcpz587sxv1BdjD9UQd9dSDYMkwJBfJq3zUei, to:EC6ui5DYvKRKRFRTNAh77NCKQ21zNBG7UrCk8aX8SST7'
# # 正则提取出接口耗时数据
# sendlist={}
# revpeopleid1 =  re.findall(r'###### (.* )recv msg',i)
# revPeopleId =revpeopleid1[0][1:-1]
# targetId = i[-44:]
# print(targetId)

# receivTime="2021-03-01 15:29:11"
# msgidList={"1":"2021-03-01 15:15:17"}
# receivTimedate=datetime.strptime(receivTime,'%Y-%m-%d %H:%M:%S')     #转换时间格式
# sendTimedate=datetime.strptime(msgidList["1"],'%Y-%m-%d %H:%M:%S')  #转换时间格式
# responseTime=(receivTimedate-sendTimedate).seconds  #计算时间差
# print(type(responseTime))
# targetId='123'
# revPeopleId='321'
# msgid='23'
# receivTime="123"
# msgidList={"1":"2321321323213"}
# responseTime=123
# outputstr=''
# outputstr=outputstr+'targetId:{},revPeopleId:{},msgid:{},sendTime：{}，receivTime：{}，responseTime:{}'.format(targetId,revPeopleId,msgid,msgidList["1"],receivTime,str(responseTime))
# print(outputstr)

# stus = [["年","月","日","a","b"],["1"],["1","2","5","6","7"],["3","4"]]

# Excel=xlwt.Workbook()#创建excel
# sheet=Excel.add_sheet("nihao")#新建标签
# row = 0
# for stu in stus:
#     col=0
#     for st in stu:
#         sheet.write(row,col,st) #开始写入
#         col+=1
#     row+=1
#
# Excel.save("123.xls")
# receivTime="2021-03-03 14:36:17.594723"
# msgidList="2021-03-03 14:36:27.247684"
# if receivTime<msgidList:
#     print(1000)
# receivTimedate=datetime.strptime(msgidList,'%Y-%m-%d %H:%M:%S.%f')     #转换时间格式
# sendTimedate=datetime.strptime(receivTime,'%Y-%m-%d %H:%M:%S.%f') #转换时间格式
# # if receivTimedate>sendTimedate:
# #     print(1)
# responseTime=(receivTimedate-sendTimedate).total_seconds()                      #计算时间差
# print(responseTime)


