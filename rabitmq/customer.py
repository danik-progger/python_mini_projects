from pika import ConnectionParameters, BlockingConnection


connection_params = ConnectionParameters(
    host="localhost",
    port=5672
)

def process_messages(ch, method, properties, body):
    print(body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    with BlockingConnection(connection_params) as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue="messages")

            ch.queue_consume(
                queue="messages",
                on_message_callback=process_messages
            )
            print("Waiting for messages")
            ch.start_consuming()


if __name__ == "__main__":
    main()