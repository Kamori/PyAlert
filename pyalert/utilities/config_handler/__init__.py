from configparser import ConfigParser

class PyAlertConfig:

    __CONFIG = {}

    def __init__(self, name, file_path):
        config = ConfigParser()
        config.read_file(open(file_path))
        _config = {name: config}
        self.__CONFIG.update(_config)

    @classmethod
    def get_config(cls):
        return cls.__CONFIG