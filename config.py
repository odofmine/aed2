import toml

with open('config.toml') as file:
    config = toml.loads(file.read())

class Config:

    @staticmethod
    def root():
        return config['root']

    @staticmethod
    def proxy():
        if Config.root()['proxy']:
            return Config.root()['proxies']
        else:
            return {}
