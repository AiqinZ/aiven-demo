import sys
import os
from unittest.mock import PropertyMock

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from unittest import TestCase, mock
from aiven_demo.model.customer import Customer
from aiven_demo.app.customer_service import CustomerService


class MockDBConnection(object):
    def __init__(self):
        pass

    def execute_sql(self, sqlStr):
        print("mock skipped: " + sqlStr)

    def close(self):
        pass


class MockDBConnectionWithException(object):
    def __init__(self):
        pass

    def execute_sql(self, sqlStr):
        raise Exception("DB error")

    def close(self):
        pass


class MockLogger(object):
    def __init__(self):
        pass

    def print(self, str):
        print("mock print")


mock_db_connection = MockDBConnection()
mock_db_connection_exception = MockDBConnectionWithException()
mock_logger = MockLogger()


class TestCustomer(TestCase):
    def setUp(self):
        self.customer = Customer(
            customer_id="5764b034-133c-11eb-9ed8-acde48001122",
            first_name="Andrew",
            last_name="Knight",
            address="579 Smith Wells South William, NV 55035",
            post_code="2077"
        )

    def test_create_customer(self):
        with mock.patch('aiven_demo.app.customer_service.CustomerService.db',
                        new_callable=PropertyMock, return_value=mock_db_connection), \
             mock.patch('aiven_demo.app.customer_service.CustomerService.logger',
                        new_callable=PropertyMock, return_value=mock_logger):
            customer_service = CustomerService()
            ret = customer_service.create_customer(self.customer)
            self.assertEqual(True, ret)

    def test_create_customer_exception(self):
        with mock.patch('aiven_demo.app.customer_service.CustomerService.db',
                        new_callable=PropertyMock, return_value=mock_db_connection_exception), \
             mock.patch('aiven_demo.app.customer_service.CustomerService.logger',
                        new_callable=PropertyMock, return_value=mock_logger):
            customer_service = CustomerService()
            ret = customer_service.create_customer(self.customer)
            self.assertEqual(False, ret)
