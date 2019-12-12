from confluent_kafka import Consumer, KafkaError
import os
from typing import List
from multiprocessing import Process, Queue
import time

config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'group4',
    'auto.offset.reset': 'earliest'
}


def consume():
    pid = os.getpid()
    c = Consumer(config)
    c.subscribe(['topic2'])
    print("pid {}".format(pid))
    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("consumer error: {}".format(msg.error()))
            continue
        print('process %s received message from %s:%s:%s: %s' % (
            pid, msg.topic(), msg.partition(), msg.offset(), msg.value()))
        time.sleep(1)


children: List[Process] = []
for i in range(0, 3):
    child = Process(target=consume, args=())
    children.append(child)
for child in children:
    child.start()
print("pussy")
