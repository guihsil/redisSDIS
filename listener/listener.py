import redis

r = redis.Redis(
    host='redis-server', 
    port=6379, 
    socket_timeout=None
)

channel = "Chat"
p = r.pubsub()
p.subscribe(channel)

for message in p.listen():
    
    if message['type'] == 'message':
        msg = message['data'].decode('utf-8')
        
        try:
            temperatura = int(msg)

            if temperatura <= 25:
                print(f"{temperatura}ºC: Tá fresquinho!")
            elif 25 < temperatura <= 32:
                print(f"{temperatura}ºC: Clima de Praia!")
            elif temperatura > 32:
                print(f"{temperatura}ºC: Um sol pra cada um!")

        except ValueError:
            print("Erro")