#!/usr/bin/env python3

import sys
import os

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from aiven_demo.db.postgre_connect import DBConnection
from aiven_demo.common.logger import Logger


class CustomerService(object):
    db = DBConnection()
    logger = Logger()

    def __init__(self):
        pass

    def create_customer(self, customer):
        try:
            sql = "insert into customers(id, first_name, last_name, address, post_code) values('%s','%s','%s','%s','%s')" \
                  % (customer.customer_id, customer.first_name, customer.last_name, customer.address, customer.post_code)

            self.db.execute_sql(sql)
            self.logger.print("DB Inserted: %s" % sql)
            return True
        except Exception as e:
            self.logger.print("An exception occurred: %s" % e)
            return False

    def modify_customer(self, customer):
        pass
