import redis

conn = redis.Redis(host="192.168.10.8", port=6379,password="398023",db=4)
conn.set(':1:_gaolinfnag','linfang·gao')

conn.client();
