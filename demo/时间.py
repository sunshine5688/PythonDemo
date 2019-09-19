import datetime

date1 = datetime.datetime.strptime(str(20190912), '%Y%m%d')
date2 = datetime.datetime.strptime(str(20200913111205), '%Y%m%d%H%M%S')
print(type(date1))

# now_date = datetime.now().strftime('%Y-%m-%d')    # 格式为str


date1.strftime('%Y%m%d')



delta = date2 - date1
print(delta.days)

