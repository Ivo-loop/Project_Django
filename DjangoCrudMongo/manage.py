#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoCrudMongo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


def start_rabbit():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='fila_projeto_Django')
    channel.basic_consume(
        queue='hello', on_message_callback=callback, auto_ack=True)


if __name__ == '__main__':
    start_rabbit()
    main()
