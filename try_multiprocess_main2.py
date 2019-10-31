import time
from logger.logger import logging


def logPing2():
    while True:
        time.sleep(1)
        logging.debug("logPing2")
