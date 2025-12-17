import redis
from random import randint
from time import sleep

r = redis.Redis(
    host='redis-server', 
    port=6379, 
    socket_timeout=None
)

channel = "Chat"
p = r.pubsub()
p.subscribe(channel)

while True:
    message = randint(15, 45)
    r.publish(channel, message)
    sleep(2)
