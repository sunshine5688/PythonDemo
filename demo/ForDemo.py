favourite = '德玛西亚'
for i in favourite:
    print(i, end=' ')
print()

member = ['盖伦','IG','艾欧尼亚','卡罗兰']
for each in member:
    print(each,len(each)) #打印字符和字符长度



for i in range(2,9):
    if i == 3:
        print('不打印3')
        continue
    if i == 5:
        print('5以后退出')
        break
    print(i)

for i in range(2,9,3): #步进为3
    print(i)