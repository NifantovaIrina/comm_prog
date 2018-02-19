import pika
import time

if __name__ == "__main__":
	print("Please wait 25 seconds")
	time.sleep(25)
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))

	channel = connection.channel()

	channel.queue_declare(queue='hello')

	channel.basic_publish(exchange='',
		              routing_key='hello',
		              body='Hello World')

	connection.close()
