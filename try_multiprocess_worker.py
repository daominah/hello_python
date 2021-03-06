from multiprocessing import Queue
import time

from logger.logger import logging


def worker(workerId: int, inChan: Queue, outChan: Queue):
    sum = 0
    while True:
        data = inChan.get(block=True, timeout=None)
        # a receive from a closed channel
        if data is None:
            inChan.put(None)
            break
        logging.debug("worker %s received data: %s" % (workerId, data))
        sum += data
        time.sleep(0.7)
    logging.info("worker %s is about to return: %s", workerId, sum)
    outChan.put(sum)
