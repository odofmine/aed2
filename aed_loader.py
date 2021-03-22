from datetime import datetime
from config import Config
from utils import Utils

class AedLoader:
    def write(self):
        now = datetime.utcnow().strftime('%Y-%m-%d')
        data = Utils.read_json(Config.aed_dir(), now)
        self.write_balance(data)

    def write_balance(self, data):
        columns = ['datetime', 'balance']
        balances = [[int(x[0][0] / 1000), int(x[0][1])] for x in data]
        Utils.write_file(f"{Config.root()['target_dir']}/data", 'balances_t4', balances, columns)

AedLoader().write()
