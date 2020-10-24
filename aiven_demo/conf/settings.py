#!/usr/bin/env python3

import configparser
import os


class ReadConfig:
    def __init__(self, file_path=None):
        if file_path:
            config_path = file_path
        else:
            root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            config_path = os.path.join(root_dir, "config_local.ini")
            if not os.path.exists(config_path):
                config_path = os.path.join(root_dir, "config.ini")

        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    def get_db(self, param):
        return self.cf.get("postgresql", param)

    def get_kafka(self, param):
        return self.cf.get("kafka", param)
