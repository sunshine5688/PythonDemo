import os
from os.path import join, getsize



# 返回指定目录的大小
def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size

if __name__ == '__main__':

    print(os.getcwd()) #得到当前工作目录
    print(os.listdir()) # 得到
    print(os.path) # 获取文件信息

    os.rmdir('./osdemo') # 删除目录
    os.mkdir('./osdemo') #创建目录
    os.chdir("./osdemo") #改变工作目录

    print(os.getcwd())

    print(os.path.getsize('../OSDemo.py')) # 得到文件大小
    os.chdir('../')
    print(os.path.getctime('./OSDemo.py')) # 得到文件的创建时间
    print(os.path.getmtime('./OSDemo.py')) #得到文件的修改时间
    print(str(getdirsize('D:\学习资料')/1024/1024/1024) + 'KB')

__author__ = 'weiran'
import os
import re


# 待检测文件大小范围必须在 1MB 以上
# 使用 du -sh 命令，以避免占用大小与真实大小不同
# 输入：待检测文件绝对路径
# 返回：该文件夹占用空间大小，单位：GB，保留2位小数
# weiran 2018-7-24
def get_doc_usage_size_by_shell(doc_path):
    response = os.popen(f'du -sh {doc_path}')
    str_size = response.read().split()[0]
    f_size = float(re.findall(r'[.\d]+', str_size)[0])
    size_unit = re.findall(r'[A-Z]', str_size)[0]
    if size_unit == 'M':
        f_size = round(f_size / 1024, 2)
    if size_unit == 'T':
        f_size = round(f_size * 1024, 2)
    return f_size


# 获取指定路径的文件夹大小（单位：GB）
def get_doc_real_size(p_doc):
    size = 0.0
    for root, dirs, files in os.walk(p_doc):
        size += sum([os.path.getsize(os.path.join(root, file)) for file in files])
    size = round(size / 1024 / 1024 / 1024, 2)
    return size
