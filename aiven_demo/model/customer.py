#!/usr/bin/env python3

import json


class Customer(object):
    def __init__(self, customer_id, first_name, last_name, address=None, post_code=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.post_code = post_code

    def __str__(self):
        return "Customer[id=%s, first_name=%s, last_name=%s, address=%s, post_code=%s" \
               % (self.customer_id, self.first_name, self.last_name, self.address, self.post_code)

    def to_json(self):
        return json.dumps(self.__dict__)
