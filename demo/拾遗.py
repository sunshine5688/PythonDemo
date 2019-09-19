class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):            # 就是类属性
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print('水池里有%d只乌龟，%d只🐟' % (self.turtle.num,self.fish.num))


if __name__ == '__main__':
    p = Pool(15,20)
    p.print_num()