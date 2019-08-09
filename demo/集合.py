# 没有映射关系的花括号 就是集合
# 元素唯一，无序不支持索引
num = {1,2,3,4,5,6,7,8,2,5,2,5,7}
print(num)
num1 = [1,2,3,4,5,6,7,8,2,5,2,5,7,0]
num1 = list(set(num1))
print(num1)
num1.add('母巢')
print(num1)