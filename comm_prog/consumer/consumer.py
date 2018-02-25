import pika
import time
import psycopg2

if __name__ == "__main__":
	print("Please wait 25 seconds")
	time.sleep(25)


	connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
	channel = connection.channel()
	channel.queue_declare(queue='hello')

	conn = psycopg2.connect(dbname='postgres', user='postgres', host='db', password='qwerty', port='5432')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS strings (str CHAR(255))")
	conn.commit()

	def callback(ch, method, properties, body):
		s = str(body, 'utf-8')
		print(" [x] Received %r" % body, flush=True)
		cur.execute("INSERT INTO strings (str) VALUES (\'{}\')".format(s))
		conn.commit()

	channel.basic_consume(callback,
		              queue='hello',
		              no_ack=True)

	channel.start_consuming()
