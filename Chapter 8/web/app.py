import time

import redis
from flask import Flask

app = Flask(__name__)


@app.route('/healthy')
def check_redis():
    try:
        r = redis.Redis(host='redis', port=6379)
        result = r.ping()

        if result == True:
            return "成功连接到redis", 200
        else:
            return "无法连接到Redis", 400
    except Exception as e:
        return f"连接错误: {str(e)}", 503
