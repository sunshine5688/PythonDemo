class Parent:
    def hello(self):
        print('正在调用父类的方法')

class Child(Parent): # 集成了Parent
    pass

class Child2(Parent):
    def hello(self):
        print('调用child2的hello方法，覆盖了父类的hello方法')
        super().hello()  # 调用父类方法

if __name__ == '__main__':
    c = Child()
    c.hello()

    c2 = Child2()
    c2.hello()
