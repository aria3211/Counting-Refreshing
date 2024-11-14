from flask import Flask
import redis
import os




app = Flask(__name__)
# os.getenv('REDIS_HOST','redis')

cache = redis.Redis(os.getenv("REDIS_HOST","redis"),port=6379)


@app.route('/')
def hello_world():  # put application's code here
    count = cache.incr('visits')
    return f'Hello Dear!, You visted this page {count} times'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
