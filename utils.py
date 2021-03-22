import math
import json
import csv
import os
import errno

from datetime import datetime

class Utils:
    @staticmethod
    def write_file(folder, file_name, data, columns):
        Utils.write_to_json(folder, file_name, data)
        Utils.write_to_csv(folder, file_name, data, columns)

    @staticmethod
    def write_to_json(folder, file_name, data):
        try:
            os.makedirs(folder)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

        with open(f'{folder}/{file_name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def read_json(folder, file_name):
        with open(f'{folder}/{file_name}.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def read_json_file(file):
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def floor(value, count=4):
        times = int(math.pow(10, count))
        return math.floor(value * times) / times

    @staticmethod
    def write_to_csv(folder, file_name, data, columns):
        try:
            os.makedirs(folder)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

        with open(f'{folder}/{file_name}.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(columns)

            for item in data:
                values = item
                if type(item) == dict:
                    values = item.values()

                func = lambda x : '{:.4f}'.format(x) if type(x) == float else x
                values = list(map(func, values))

                if columns[0] == 'datetime':
                    value = values[0]
                    if type(value) == str:
                        value = float(value)
                    values[0] = datetime.utcfromtimestamp(int(value))
                writer.writerow(values)
