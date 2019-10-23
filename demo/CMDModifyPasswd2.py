# encoding UTF-8
import telnetlib, sys
from time import sleep
import threading

def telnetdo(HOST=None, USER=None, PASS=None, COMMAND=None): #define a function

    tn = telnetlib.Telnet() #
    try:
        tn.open(HOST)

    except Exception as ex:
        print(ex.args)
        print("Cannot open host")
        return

    tn.write('\r\n')
    tn.read_until("login:")
    tn.write(USER+'\r\n')
    print(tn.read_until("password:"))
    tn.write(PASS +'\r\n')
    print(tn.read_until(">"))
    result = tn.write(COMMAND + '\r\n')

    print(result)

    tmp = tn.read_all()
    tn.close()
    return tmp.decode('GBK')

if __name__ == '__main__':
    t1=threading.Thread(target=telnetdo,args=('192.168.253.135','gaolinfang','000','ipconfig'))
    t1.setDaemon(True)
    t1.start()
    print('*****************')
    #do something test
    sleep(90)