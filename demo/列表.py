mix = [1,'李察·阿克德蒙',3.14,{'name':'千夜'},[666,2]]
mix.append('深蓝')
print(len(mix))

mix.extend(['苏海伦','山与海'])
print(len(mix))

print(mix)

mix.insert(0,'流沙')
print(mix)

mix.remove(3.14)#删除元素
print(mix)

del mix[1] #删除对应下标
print(mix)

print(mix.pop()) #将最后一个元素取出
print(mix)

print(mix.pop(1)) #取出指定下标元素
print(mix)


mix2 = mix[2:3]#得到一个新列表，为原来列表的2到3的之间元素，不包含2，包含3
print(mix2)

#print(mix > mix2)#列表的比较与字符串比较类似，从第一元素开始比较，但是对应元素必须能够比较

print('流沙' in mix)
print('流沙' not in mix)

#查找元素下标
print(mix.index('深蓝'))

list2 = [2,5,3,1,8,3]
list2.sort() #从小到大排队
print(list2)
list2.reverse() # 反转
print(list2)