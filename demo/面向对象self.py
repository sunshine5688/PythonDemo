class Ball:
    def setName(self,name):
            self.name = name
    def kick(self):
        print("我叫%s，该死的，谁踢我。。。" % self.name)

if __name__ == '__main__':
    a = Ball()
    a.setName('球A')
    a.kick()
