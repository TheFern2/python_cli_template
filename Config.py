import configparser

class Config:
    config = configparser.ConfigParser()
    config.read("Settings.ini")
    app_name = ""
    version = ""

    @classmethod
    def read_settings(cls):
        cls.app_name = cls.config["Settings"]["app_name"]
        cls.version = cls.config["Settings"]["version"]
