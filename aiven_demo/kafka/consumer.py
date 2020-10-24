#!/usr/bin/env python3

import json
import sys
import os
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from kafka import KafkaConsumer
from time import sleep
from aiven_demo.model.customer import Customer
from aiven_demo.app.customer_service import CustomerService
from aiven_demo.conf.settings import ReadConfig
from aiven_demo.common.logger import Logger

logger = Logger()
config = ReadConfig()

param_bootstrap_servers = config.get_kafka("servers")
param_topic_id = config.get_kafka("topic")
param_group_id = config.get_kafka("group_id")
param_auto_offset_reset = config.get_kafka("auto_offset_reset")
param_security_protocol = "PLAINTEXT"
param_ssl_cafile = None
param_ssl_certfile = None
param_ssl_keyfile = None

if config.get_kafka('ssl').upper() == "TRUE":
    param_security_protocol = "SSL"
    param_ssl_cafile = config.get_kafka("ssl_cafile")
    param_ssl_certfile = config.get_kafka("ssl_certfile")
    param_ssl_keyfile = config.get_kafka("ssl_keyfile")

consumer = KafkaConsumer(
    param_topic_id,
    group_id=param_group_id,
    bootstrap_servers=param_bootstrap_servers,
    auto_offset_reset=param_auto_offset_reset,
    security_protocol=param_security_protocol,
    ssl_cafile=param_ssl_cafile,
    ssl_certfile=param_ssl_certfile,
    ssl_keyfile=param_ssl_keyfile
)

try:
    print("Kafka consumer begins...")
    for msg in consumer:
        logger.print("Received: %s" % (msg.value))
        customer_dict = json.loads(msg.value)
        customer = Customer(**customer_dict)
        customer_service = CustomerService()
        customer_service.create_customer(customer)
        sleep(0.5)
except KeyboardInterrupt as e:
    print("Stopped.")
