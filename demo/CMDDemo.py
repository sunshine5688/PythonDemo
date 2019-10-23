import winrm
# wintest = winrm.Session('http://192.168.253.135:5985/wsman',auth=('gaolinfang','123'))
wintest = winrm.Session('http://10.0.47.123:5985/wsman',auth=('admin','Uni@sec123'))
r = wintest.run_cmd('ipconfig')
# r = wintest.run_cmd('net user gaolinfang 123')
# print(r.std_out)
# print(r.std_err)


    # 注意：需要在被控机上开启以下服务：
    # 针对winrm service 进行基础配置：
    # winrm quickconfig
    # 查看winrm service listener:
    # winrm e winrm/config/listener
    # 为winrm service 配置auth:
    # winrm set winrm/config/service/auth @{Basic="true"}
    # 为winrm service 配置加密方式为允许非加密：
    # winrm set winrm/config/service @{AllowUnencrypted="true"}
    # '''
# https://blog.csdn.net/weixin_30260399/article/details/98940653