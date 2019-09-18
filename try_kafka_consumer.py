from confluent_kafka import Consumer, KafkaError
import os
from typing import List
from multiprocessing import Process, Queue
import time

config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup2',
    'auto.offset.reset': 'earliest'
}


def consume():
    pid = os.getpid()
    c = Consumer(config)
    c.subscribe(['test2'])
    print("pid {}".format(pid))
    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        print('Process {} received message: {}'.format(
            pid, msg.value().decode('utf-8')))
        time.sleep(2)


children: List[Process] = []
for i in range(0, 3):
    child = Process(target=consume, args=())
    children.append(child)
for child in children:
    child.start()
print("pussy")
