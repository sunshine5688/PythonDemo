import os

cmd = 'cd /opt/jumpserver/data/ && zip {0}.zip {0}.csv -P {1} && cp {0}.zip /opt/jumpserver/data'\
                .format('改密计划2', '123456')

print(cmd)
ret = os.popen(cmd)
result = ret.read()

print(result)