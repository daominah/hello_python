import datetime
import time
import logging
from tradex_common_python.kafka.Producer import BaseProducer
from tradex_common_python import init_log_to_console

init_log_to_console(log_level=logging.DEBUG,
                    log_format="%(asctime)s:%(levelname)-8s:[%(filename)s:%(lineno)d] %(message)s")

producer: BaseProducer = BaseProducer({"bootstrap.servers": '127.0.0.1:9092'})

for i in range(0, 1):
    producer.send(
        topic="topic01",
        message={"msg": "msg%s" % datetime.datetime.now().isoformat()},
    )
    producer.producer.flush()
    logging.debug("done")
