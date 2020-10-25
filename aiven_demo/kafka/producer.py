#!/usr/bin/env python3

import time
import uuid
import sys
import os


root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from faker import Faker
from aiven_demo.model.customer import Customer
from aiven_demo.conf.settings import ReadConfig
from aiven_demo.common.logger import Logger
from kafka import KafkaProducer
from kafka.errors import KafkaError


config = ReadConfig()


param_bootstrap_servers = config.get_kafka("servers")
param_security_protocol = "PLAINTEXT"
param_ssl_cafile = None
param_ssl_certfile = None
param_ssl_keyfile = None
if config.get_kafka('ssl').upper() == "TRUE":
    param_security_protocol = "SSL"
    param_ssl_cafile = config.get_kafka("ssl_cafile")
    param_ssl_certfile = config.get_kafka("ssl_certfile")
    param_ssl_keyfile = config.get_kafka("ssl_keyfile")

producer = KafkaProducer(
    bootstrap_servers=param_bootstrap_servers,
    security_protocol=param_security_protocol,
    ssl_cafile=param_ssl_cafile,
    ssl_certfile=param_ssl_certfile,
    ssl_keyfile=param_ssl_keyfile
)

topic = config.get_kafka("topic")

logger = Logger()
fake = Faker()


def produce():
    """Function using Faker library to generate events and write to topic in Kafka."""
    print('producer begins')
    try:
        while True:
            customer = Customer(
                customer_id=uuid.uuid1().__str__(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                address=fake.address(),
                post_code="2077"
            )
            json_str = customer.to_json()
#            print(json_str)
            producer.send(topic, json_str.encode())
            logger.print("Sent: " + json_str)
            time.sleep(2)
    except KafkaError as e:
        print(e)
    finally:
        producer.close()
        print('producer existed')


if __name__ == '__main__':
    produce()
