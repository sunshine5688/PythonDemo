# encoding=utf-8
import telnetlib
import time


def do_telnet(Host, username, password, finish, command):
    # 连接Telnet服务器
    tn = telnetlib.Telnet(Host, port=23, timeout=10)

    # timeout只是在初始化socket连接时起作用，而一旦连接成功后出现等待就不起作用了，
    # 比如使用read_until方式获取内容时返回的内容与指定的内容不符合，那么就会造成提示等待的情况，这时timeout是不起作用的，
    # 这个socket连接会一直保持着，永生不死.一种解决方案是，使用threading模块，利用线程模式来解决.
    tn.set_debuglevel(2)

    # 输入登录用户名
    tn.read_until('ENTER USERNAME < ')
    tn.write(username + '\r\n')

    # 输入登录密码
    tn.read_until('ENTER PASSWORD < ')
    tn.write(password + '\r\n')

    # 登录完毕后执行命令
    tn.read_until(finish)
    result = tn.write('%s\r\n' % command);
    print("00000000000000000000000000000000")
    print(result)

    # 执行完毕后，终止Telnet连接（或输入exit退出）
    tn.read_until('COMMAND EXECUTED')
    tn.close()  # tn.write('exit\n')

if __name__ == '__main__':
    # 配置选项
    Host = '192.168.253.135'  # Telnet服务器IP
    username = 'gaolinfang'  # 登录用户名
    password = '000'  # 登录密码
    finish = 'LEVEL COMMAND <___>'  # 命令提示符
    command = 'ipconfig;'
    do_telnet(Host, username, password, finish, command)