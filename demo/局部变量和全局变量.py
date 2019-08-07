count = 5
def modify():
    count = 10
    print('执行modify')

def modify2():
    global count
    count = 11
    print('执行modify2')


if __name__ == '__main__':
    modify()
    print(count)
    modify2()
    print(count)