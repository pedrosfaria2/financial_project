import pika
import time


def callback(ch, method, properties, body):
    print(f"Received {body}")

    time.sleep(1)
    print("Data collected")


connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='data_queue')

channel.basic_consume(queue='data_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
