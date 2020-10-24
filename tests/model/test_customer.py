import unittest
import json
import sys
import os
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from aiven_demo.model.customer import Customer


class TestCustomer(unittest.TestCase):

    def test_customer_to_json(self):
        customer = Customer(
            customer_id="5764b034-133c-11eb-9ed8-acde48001122",
            first_name="Andrew",
            last_name="Knight",
            address="579 Smith Wells South William, NV 55035",
            post_code="2077"
        )
        json_str = customer.to_json()
        expected = '{"customer_id": "5764b034-133c-11eb-9ed8-acde48001122", "first_name": "Andrew", '\
                   '"last_name": "Knight", "address": "579 Smith Wells South William, NV 55035", "post_code": "2077"}'
        self.assertEqual(expected, json_str)

    def test_json_to_customer(self):
        json_str = '{"customer_id": "5764b034-133c-11eb-9ed8-acde48001122", "first_name": "Andrew", '\
                   '"last_name": "Knight", "address": "579 Smith Wells South William, NV 55035", "post_code": "2077"}'
        customer_dict = json.loads(json_str)
        customer = Customer(**customer_dict)
        self.assertEqual("5764b034-133c-11eb-9ed8-acde48001122", customer.customer_id)
        self.assertEqual("Andrew", customer.first_name)
        self.assertEqual("Knight", customer.last_name)
        self.assertEqual("579 Smith Wells South William, NV 55035", customer.address)
        self.assertEqual("2077", customer.post_code)
