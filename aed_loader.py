from datetime import datetime
from config import Config
from utils import Utils

class AedLoader:
    def write(self):
        now = datetime.utcnow().strftime('%Y-%m-%d')
        data = Utils.read_json(Config.aed_dir(), now)
        key = 'trendfund-t4'
        self.write_balance(key, data)

        key = 'jiuyao-91_2106'
        data = Utils.read_json(f'{Config.aed_dir()}/jiuyao', now)
        self.write_balance(key, data)

    def write_exchanges_info():
        pass

    def write_balance(self, key, data):
        columns = ['datetime', 'balance']
        balances = [[int(x[0][0] / 1000), int(x[0][1])] for x in data]
        Utils.write_file(f"{Config.root()['target_dir']}/data", f'balances_{key}', balances, columns)

AedLoader().write()
