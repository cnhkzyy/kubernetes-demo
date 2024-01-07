import time
import random
import redis
from flask import Flask

app = Flask(__name__)




@app.route('/healthy')
def check_redis():
    try:
        hosts= ["192.168.1.125", "192.168.1.155"]
        host = random.choice(hosts)
        r = redis.Redis(host=host, port=30001)
        result = r.ping()
        print(f"host: {host}, result: {result}")

        if result == True:
            return "成功连接到redis", 200
        else:
            return "无法连接到Redis", 400
    except Exception as e:
        return f"连接错误: {str(e)}", 503


app.run()
