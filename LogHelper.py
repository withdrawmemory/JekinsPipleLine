import time

def LogHelper.SaveLog(saveName):
    #写入文件，二进制的方式
    file = open(saveName, 'wb')
    file.write("测试\n".encode("UTF-8"))
    localtime = "当前时间：" + str(time.localtime(time.time()))
    file.write(localtime.encode("UTF-8"))
    file.close()