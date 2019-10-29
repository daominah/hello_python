from multiprocessing import Process, Queue

from logger.logger import logging

from try_multiprocess_worker import worker


def main():
    nWorkers = 4
    inChan, outChan = Queue(), Queue()
    for i in range(nWorkers):
        child = Process(target=worker, args=(i, inChan, outChan))
        child.start()
    logging.warning("starting the main")
    for i in range(10):
        inChan.put(i)
    inChan.put(None)
    sum = 0
    for i in range(nWorkers):
        r = outChan.get(block=True, timeout=None)
        sum += r
    logging.warning("sum: %s" % sum)


main()
