import time
import random
import pika
count_message = 1
credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('192.168.1.123',5672,'/', credentials)
connection = pika.BlockingConnection(parameters) 
channel = connection.channel()
channel.queue_declare(queue='IntQueue')


while True:
    random_int = [random.randint(0,10) for _ in range(2)]
    message = ''.join(map(str, random_int))
    channel.basic_publish(exchange='', routing_key='IntQueue', body=message)

    print "Published Message ",count_message
    count_message+=1
    time.sleep(1)
connection.close()


    
