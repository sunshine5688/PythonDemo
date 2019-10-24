#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################
# author: SkyJ
# date  : 2019/7/17
################################################

import os
import sys
import string
import datetime
import time
import paramiko  # 导入paramiko

# hostname = "10.0.47.123"
# username = "admin"
# password = "Uni@sec123"
# cmdList = ['ipconfig']

hostname = "192.168.253.135"
username = "gaolinfang"
password = "000"
cmdList = ['net user gaolinfang 000']

# hostname = "10.0.47.111"
# username = "user"
# password = "Uni@sec66998"
# cmdList = ['ipconfig']

# hostname = "10.0.47.124"
# username = "user"
# password = "Uni@sec66998"
# cmdList = ['dir']

# 第二种ssh连接执行指令方式
def sshRunCmd2(hostname, username, password, cmdList):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 创建ssh连接
        client.connect(hostname=hostname, port=22, username=username, password=password)
        # 执行指令
        for cmd in cmdList:
            stdin, stdout, stderr = client.exec_command(cmd)
            result = stdout.read()
            result = result.decode('GBK', "ignore")
            print(result)
    except Exception as e:
        print("[%s] %s target failed, the reason is %s" % (datetime.datetime.now(), hostname, str(e)))
    else:
        print("[%s] %s target success" % (datetime.datetime.now(), hostname))
    finally:
        client.close()


if __name__ == '__main__':
    sshRunCmd2(hostname, username, password, cmdList)



# https://gsf-fl.softonic.com/258/665/d8e2a640359f63c9f4dc3b70dccfaa3c50/file?Expires=1571851822&Signature=6d2307d881d5060fa51dccd3a7258a6e78b850d0&SD_used=&channel=WEB&fdh=no&id_file=0973b12a-96d8-11e6-b284-00163ec9f5fa&instance=softonic_en&type=PROGRAM&url=https://openssh.en.softonic.com&Filename=setupssh.exe
# https://en.softonic.com/download/openssh/windows/post-download

# https://www.jianshu.com/p/6e5bc39d386e

# 进入链接下载最新 OpenSSH-Win64.zip（64位系统），解压至C:\Program Files\OpenSSH
#
# 2、打开cmd，cd进入C:\Program Files\OpenSSH（安装目录），执行命令：
#
# powershell.exe -ExecutionPolicy Bypass -File install-sshd.ps1
#
# 3、设置服务自动启动并启动服务：
#
# sc config sshd start= auto
#
# net start sshd

# 防火墙打开22端口

