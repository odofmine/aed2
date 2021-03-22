import toml

with open('config.toml') as file:
    config = toml.loads(file.read())

class Config:

    @staticmethod
    def root():
        return config['root']

    @staticmethod
    def aed_dir():
        return Config.root()['aed_dir']
