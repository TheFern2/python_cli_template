import logging
import time

from Config import Config
from tap import Tap

class MyArgumentParser(Tap):
    test_arg: str = 'Hello!'

class App:
    logger = logging.getLogger("console")
    args = MyArgumentParser().parse_args()

    @classmethod
    def run(cls):
        while True:
            cls.logger.info(f"App running")
            time.sleep(1)

    @classmethod
    def init(cls):
        cls.init_logging()
        Config.read_settings()
        cls.logger.info(f"App {Config.app_name} {Config.version} initialized")

    @classmethod
    def init_logging(cls):
        cls.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        cls.logger.addHandler(ch)

