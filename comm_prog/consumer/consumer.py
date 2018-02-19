import pika
import time

if __name__ == "__main__":
	print("Please wait 25 seconds")
	time.sleep(25)
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
	channel = connection.channel()

	channel.queue_declare(queue='hello')

	def callback(ch, method, properties, body):
	    print(" [x] Received %r" % body, flush=True)
	

	channel.basic_consume(callback,
		              queue='hello',
		              no_ack=True)

	channel.start_consuming()
