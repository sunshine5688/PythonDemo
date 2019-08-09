class Ball:
    def __init__(self,name): # 构造器
        self.name = name

    def kick(self):
        print("我叫%s，该死的，谁踢我。。。" % self.name)



class Person:
    name = "小乌龟"  #public变量
    __age = 28       #private变量   伪私有变量，只是被改名字了，python没有访问控制概念

    def getAge(self):
        return self.__age


if __name__ == '__main__':
    a = Ball('球A')
    a.kick()

    p = Person()
    print(p.name)
    print(p.getAge())
    print(p._Person__age) # 被改名的私有变量