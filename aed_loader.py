from datetime import datetime
from config import Config
from utils import Utils

import requests

class AedLoader:
    def __init__(self) -> None:
        self.exchange_info_url = 'https://littleee.com/api/{exchange}Info'

    def write(self):
        now = datetime.utcnow().strftime('%Y-%m-%d')
        data = Utils.read_json(Config.aed_dir(), now)
        self.write_balance('trendfund', 't4', data)

        data = Utils.read_json(f'{Config.aed_dir()}/jiuyao', now)
        self.write_balance('jiuyao', '91_2106', data)

        self.write_exchanges_info('trendfund', 't4', ['ftx', 'binance', 'deribit', 'kraken'])
        self.write_exchanges_info('jiuyao', '91_2106', ['jiuyao'])

    def write_exchanges_info(self, manager, code, exchanges):
        for exchange in exchanges:
            resp = requests.get(self.exchange_info_url.format(exchange=exchange)).json()
            Utils.write_to_json(f"{Config.root()['target_dir']}/data/{manager}/{code}", exchange, resp)

    def write_balance(self, manager, code, data):
        columns = ['datetime', 'balance']
        balances = [[int(x[0][0] / 1000), int(x[0][1])] for x in data]
        Utils.write_file(f"{Config.root()['target_dir']}/data/{manager}/{code}", 'balances', balances, columns)

    def exchange_info_format(self, data):
        return {
            'current_leverage': self.format(data[0]),
            'balance': {
                'btc': self.format(data[1]),
                'usd': self.format(data[2])
            },
            'account_unrealized_pnl': self.format(data[3]),
            'margin_balance': self.format(data[4]),
            'avaliable_balance': self.format(data[5]),
            'market_value': self.format(data[6]),
            'symbol': self.format(data[7]),
            'exchange_max_leverge': self.format(data[8]),
            'contract_value': self.format(data[10]),
            'position': {
                'qty': self.format(data[9]),
                'avg_price': self.format(data[11]),
                'unrealized_pnl': self.format(data[12]),
                'max_long_qty': self.format(data[13]),
                'max_short_qty': self.format(data[14]),
            }
        }

    def format(self, item):
        return item if not item == None else 0.0

AedLoader().write()
