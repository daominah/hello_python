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
import os
import logging as pylog
import logging.handlers as pyhandlers
import multiprocessing
from distutils.util import strtobool

# debug
os.environ["PYTHON_LOG_ROTATE"] = "False"

# read env vars
logLevel = pylog.DEBUG
if "PYTHON_LOG_LEVEL" in os.environ:
    if os.environ["PYTHON_LOG_LEVEL"] in pylog._nameToLevel:
        logLevel = pylog._nameToLevel[os.environ["PYTHON_LOG_LEVEL"]]
isLogBoth = True
if "PYTHON_LOG_BOTH" in os.environ:
    isLogBoth = strtobool(os.environ["PYTHON_LOG_BOTH"])
isLogRotate = False
if "PYTHON_LOG_ROTATE" in os.environ:
    isLogRotate = strtobool(os.environ["PYTHON_LOG_ROTATE"])
logFilePath = ""
if "PYTHON_LOG_FILE" in os.environ:
    logFilePath = os.environ["PYTHON_LOG_FILE"]

# apply config to the root logger
logging = pylog.getLogger()
logging.setLevel(logLevel)
handlers: [pylog.Handler] = []
stdoutHandle = pylog.StreamHandler(sys.stdout)
if logFilePath == "":
    handlers = [stdoutHandle]
else:
    if not isLogRotate:
        fileHandler = pylog.FileHandler(logFilePath)
    else:
        fileHandler = pyhandlers.TimedRotatingFileHandler(
            logFilePath, when='S', interval=2, delay=0)
    if isLogBoth:
        handlers = [fileHandler, stdoutHandle]
    else:
        handlers = [fileHandler]
for h in handlers:
    h.setFormatter(pylog.Formatter(
        "%(asctime)s: %(levelname)-5s %(filename)s:%(lineno)d: %(message)s"))
logging.handlers = handlers
