import os
from abc import ABC, abstractmethod

# Before: Each source has its own load-parse-validate pipeline
class AppConfig:
    def __init__(self):
        self.file_config = {"db.host": "localhost", "db.port": "5432"}
        self.defaults = {"db.host": "127.0.0.1", "db.port": "3306", "db.timeout": "30"}

    def get_from_file(self, key: str):
        value = self.file_config.get(key)
        if value is None or value == "":  # Duplicated validation
            return None
        return value

    def get_from_env(self, key: str):
        value = os.environ.get(key.replace(".", "_").upper())
        if value is None or value == "":  # Duplicated validation
            return None
        return value

    def get_from_defaults(self, key: str):
        value = self.defaults.get(key)
        if value is None or value == "":  # Duplicated validation
            return None
        return value
    
class ConfigSource(ABC):

    @abstractmethod
    def load_value(self):
        pass

class FileLoader(ConfigSource):
    def __init__(self, config):
        self.config = config

    def load_value(self, key):
        return self.config.get(key)


class EnvLoader(ConfigSource):
    
    def load_value(self, key: str):
        return os.environ.get(key.replace(".", "_").upper())

class DefaultLoader(ConfigSource):

    def __init__(self, defaults):
        self.defaults = defaults

    def load_value(self, key):
        return self.defaults.get(key)
    
class ConfigLoader():

    def __init__(self, loaders):
        self.loaders = loaders
    
    def get(self, key):
        for source in self.loaders:
            value = source.load_value(key)
            if value is not None and value != "":
                return value
        return None

# TODO: Extract a ConfigSource interface (ABC) and create a ConfigLoader.


if __name__ == "__main__":
    file_config = {"db.host": "localhost", "db.port": "5432"}
    defaults = {"db.host": "127.0.0.1", "db.port": "3306", "db.timeout": "30"}

    loader = ConfigLoader([
        FileLoader(file_config),
        EnvLoader(),
        DefaultLoader(defaults),
    ])

    print(f"db.host = {loader.get('db.host')}")
    print(f"db.port = {loader.get('db.port')}")
    print(f"db.timeout = {loader.get('db.timeout')}")