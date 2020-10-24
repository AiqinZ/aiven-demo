#!/usr/bin/env python3

import psycopg2
import sys
import os

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from aiven_demo.conf.settings import ReadConfig


class DBConnection:
    def __init__(self):
        self.config = ReadConfig()
        self.conn = None
        self.cursor = None

    def connect(self):
        host = self.config.get_db("host")
        port = self.config.get_db("port")
        user = self.config.get_db("user")
        password = self.config.get_db("password")
        dbname = self.config.get_db("dbname")
        self.conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )
        self.cursor = self.conn.cursor()

    def execute_sql(self, sqlstr):
        self.connect()
        self.cursor.execute(sqlstr)
        self.conn.commit()
        self.close()

    def query(self, sql):
        self.connect()
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
