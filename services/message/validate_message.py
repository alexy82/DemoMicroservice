# coding=utf-8
import sys

import os
import json
import logging
import datetime

from demomc import settings
from MQ.consumers import BasicConsumer

LOGGER = logging.getLogger('main')


class MyConsumer(BasicConsumer):
    """Validate messages"""

    def message_process(self, channel, method_frame, header_frame, body: bytes):
        print('routing_key: {}'.format(method_frame.routing_key))
        body = body.decode()
        print(body)
        book = json.loads(body)
        print(book)


if __name__ == '__main__':
    print("Start Consuming...")
    queue_name = 'book'
    consumer = MyConsumer(queue_name=queue_name)
    consumer.start()
