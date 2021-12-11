import pika, sys, os
def main():
	credentials = pika.PlainCredentials('admin', 'admin')
	parameters = pika.ConnectionParameters('192.168.1.123',5672,'/', credentials)

	connection = pika.BlockingConnection(parameters)   
	channel = connection.channel()
	channel.queue_declare(queue='IntQueue')
	def callback(ch,method,properities,body):
	    comming_message = str(body).strip()
	    
	    num_1 =  int(comming_message[0])
	    num_2 =  int(comming_message[1])
	    print "The Multiplication of ",num_1, 'and', num_2, ' is: ',num_1 * num_2
	    print '.'*50, '\n'
	 

	channel.basic_consume(
	    callback,queue='IntQueue',no_ack=True
	)
	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)