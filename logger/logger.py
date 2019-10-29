"""
This package is a helper for init logger from environment vars.
Usage: from logger.logger import logging
Config:
    PYTHON_LOG_LEVEL: default is debug
    PYTHON_LOG_FILE: default log to stdout
    PYTHON_LOG_BOTH: log simultaneously to both stdout and file, default is True
"""

import sys
import os
import logging as pylog

logging = pylog.getLogger()

logLevel = pylog.DEBUG
if "PYTHON_LOG_LEVEL" in os.environ:
    if os.environ["PYTHON_LOG_LEVEL"] in pylog._nameToLevel:
        logLevel = pylog._nameToLevel[os.environ["PYTHON_LOG_LEVEL"]]
logging.setLevel(logLevel)

isLogBoth = True
if "PYTHON_LOG_BOTH" in os.environ:
    isLogBoth = bool(os.environ["PYTHON_LOG_BOTH"])

handlers: [pylog.Handler] = []
stdoutHandle = pylog.StreamHandler(sys.stdout)
if "PYTHON_LOG_FILE" not in os.environ:
    handlers = [stdoutHandle]
else:
    fileHandler = pylog.FileHandler(os.environ["PYTHON_LOG_FILE"])
    if isLogBoth:
        handlers = [fileHandler, stdoutHandle]
    else:
        handlers = [fileHandler]
for h in handlers:
    h.setFormatter(pylog.Formatter(
        "%(asctime)s: %(levelname)-5s %(filename)s:%(lineno)d: %(message)s"))
logging.handlers = handlers
