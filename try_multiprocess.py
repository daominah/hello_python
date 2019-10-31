from multiprocessing import Process, Queue
from threading import Thread
import time

from logger.logger import logging
from try_multiprocess_worker import worker
import try_multiprocess_main2


def logPing():
    while True:
        time.sleep(1)
        logging.debug("")


Thread(target=logPing, daemon=True).start()
Thread(target=try_multiprocess_main2.logPing2, daemon=True).start()

nWorkers = 2
inChan, outChan = Queue(), Queue()
children: [Process] = []
for i in range(nWorkers):
    child = Process(target=worker, args=(i, inChan, outChan))
    child.start()
    children.append(child)
logging.warning("starting the main")
for i in range(10):
    inChan.put(i)
inChan.put(None)
sum = 0
for i in range(nWorkers):
    try:
        r = outChan.get(block=True, timeout=None)
        sum += r
    except:
        pass
logging.warning("sum: %s" % sum)

for child in children:
    child.join()
logging.warning("done")
