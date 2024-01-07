import time
import socket
import redis
from flask import Flask

app = Flask(__name__)

hostname = socket.gethostname()



@app.route('/healthy')
def check_redis():
    host = None
    try:
        if hostname == "k8s-node1":
            host = "192.168.1.125"
        elif hostname == "k8s-node2":
            host = "192.168.1.155"
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
