import logging
import time
import argparse

from CustomFormatter import CustomFormatter
from Config import Config

class App:
    logger = logging.getLogger("console")
    args = None

    @classmethod
    def run(cls):
        while True:
            cls.logger.info(f"App running")
            time.sleep(1)

    @classmethod
    def init(cls):
        cls.init_logging()
        cls.init_args()
        Config.read_settings()
        cls.logger.info(f"App {Config.app_name} {Config.version} initialized")

    @classmethod
    def init_logging(cls):
        cls.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(CustomFormatter())
        cls.logger.addHandler(ch)


    @classmethod
    def init_args(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument('test_arg', nargs='?', help="Test argument")
        cls.args = parser.parse_args()
