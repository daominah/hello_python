import datetime
import time
import logging

from tradex_common_python.kafka.Producer import CommonSender
from tradex_common_python import init_log_to_console

init_log_to_console(log_level=logging.DEBUG, log_format="%(asctime)s:%(levelname)-8s:[%(filename)s:%(lineno)d] %(message)s")

source_id = "tuxbr-listener"
producer: CommonSender = CommonSender({
    "bootstrap.servers": '127.0.0.1:9092',
    # "bootstrap.servers": 'localhost:9092',
    "batch.num.messages": 5,
}, source_id)

producer.send(
    tx_id=datetime.datetime.utcnow().isoformat(),
    topic="notification:",
    uri="/uri0",
    message_type="MESSAGE",
    body={"data": "data0"},
    key="username0")

time.sleep(5)
logging.debug("done")