"""
This package is a helper for init logger from environment vars.
Usage: from logger.logger import logging
Config:
    PYTHON_LOG_LEVEL: default is debug
    PYTHON_LOG_FILE: default log to stdout
    PYTHON_LOG_BOTH: log simultaneously to both stdout and file, default is True
    PYTHON_LOG_ROTATE: rotating the log file by time or size
"""

import sys
import logging as pylog
import logging.handlers as pyhandlers
from distutils.util import strtobool
import multiprocessing
import time
import os


class LogConfig:

    def __init__(self, logLevel=pylog.DEBUG, logFilePath="", isLogRotate=True,
                 isLogBoth=True):
        self.logLevel = logLevel
        # default log to stdout
        self.logFilePath = logFilePath
        # whether to log simultaneously to both stdout and file
        self.isLogBoth = isLogBoth
        # whether to rotate log file at midnight
        self.isLogRotate = isLogRotate


class MultiprocTimedRotatingFileHandler(pyhandlers.TimedRotatingFileHandler):
    """Multiprocessing aware.
    Only rotate log file on MainProcess, children just reopen"""

    def doRollover(self):
        oldStream = self.stream
        # get the time that this sequence started at and make it a TimeTuple
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        dfn = self.rotation_filename(self.baseFilename + "." +
                                     time.strftime(self.suffix, timeTuple))
        if multiprocessing.current_process().name == "MainProcess":
            os.rename(self.baseFilename, dfn)
        if not self.delay:
            self.stream = self._open()
            if oldStream:
                oldStream.close()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        # If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith(
                'W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:  # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt


def ApplyOnRootLogger(conf: LogConfig) -> pylog.Logger:
    logging = pylog.getLogger()
    logging.setLevel(conf.logLevel)
    handlers: [pylog.Handler] = []
    stdoutHandle = pylog.StreamHandler(sys.stdout)
    if conf.logFilePath == "":
        handlers = [stdoutHandle]
    else:
        if not conf.isLogRotate:
            fileHandler = pylog.FileHandler(conf.logFilePath)
        else:
            when = "S"
            # when = "MIDNIGHT"
            fileHandler = MultiprocTimedRotatingFileHandler(
                conf.logFilePath, when=when, interval=1)
        if conf.isLogBoth:
            handlers = [fileHandler, stdoutHandle]
        else:
            handlers = [fileHandler]
    for h in handlers:
        h.setFormatter(pylog.Formatter(
            "%(asctime)s: %(levelname)-5s %(filename)s:%(lineno)d: %(message)s"))
    logging.handlers = handlers
    return logging


def LoadLogConfigFromEnv() -> LogConfig:
    self = LogConfig()
    if "PYTHON_LOG_LEVEL" in os.environ:
        temp = os.environ["PYTHON_LOG_LEVEL"]
        if temp in pylog._nameToLevel:
            self.logLevel = pylog._nameToLevel[temp]
    if "PYTHON_LOG_BOTH" in os.environ:
        self.isLogBoth = strtobool(os.environ["PYTHON_LOG_BOTH"])
    if "PYTHON_LOG_ROTATE" in os.environ:
        self.isLogRotate = strtobool(os.environ["PYTHON_LOG_ROTATE"])
    if "PYTHON_LOG_FILE" in os.environ:
        self.logFilePath = os.environ["PYTHON_LOG_FILE"]
    return self


logging = ApplyOnRootLogger(LoadLogConfigFromEnv())
