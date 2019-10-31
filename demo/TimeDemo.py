import datetime
import time

dt = datetime.datetime.now()
begintime = dt.strftime("%Y-%m-%d %H")
begintime = datetime.datetime.strptime(begintime, "%Y-%m-%d %H")
endtime = begintime + datetime.timedelta(hours=1)


print("1.把datetime转成字符串: ", begintime)
print("2.把字符串转成datetime: ", begintime)
print("2.把字符串转成datetime: ", endtime)