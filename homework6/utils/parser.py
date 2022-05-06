import pathlib
from collections import Counter
from models.models import *

CONST_IP = 0
CONST_TYPE = 5
CONST_URL = 6
CONST_CODE = 8
CONST_SIZE = 9


def log_to_str():
    dir_path = pathlib.Path.cwd()
    file_path = (pathlib.Path(dir_path, 'access.log'))
    with open(file_path) as file:
        for line in file:
            yield line


class Parser:

    @staticmethod
    def parse(model):

        if model == TotalAmountRequestsModel:
            """Общее количество запросов"""
            n = 0
            for _ in log_to_str():
                n += 1
            return [{'number': n}]

        if model == AmountByTypeRequestsModel:
            """Общее количество запросов по типу"""
            urls = []
            result = []
            for line in log_to_str():
                method = line.split()[CONST_TYPE][1::]
                if len(method) > 8:
                    continue
                urls.append(method)
            for key, value in Counter(urls).most_common():
                result.append({'method': key, 'number': value})
            return result

        if model == Top10FrequentRequestsModel:
            """Топ 10 самых частых запросов"""
            urls = []
            result = []
            for line in log_to_str():
                urls.append(line.split()[CONST_URL])
            for key, value in Counter(urls).most_common(10):
                result.append({'url': key, 'number': value})
            return result

        if model == Top5LargestRequestsWithClientErrorModel:
            """Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой"""
            urls = []
            result = []
            for line in log_to_str():
                splitted = line.split()
                if int(splitted[CONST_CODE]) // 100 == 4:
                    urls.append([splitted[CONST_IP], splitted[CONST_URL], splitted[CONST_CODE], splitted[CONST_SIZE]])
            urls = sorted(urls, key=lambda tup: int(tup[3]), reverse=True)
            for line in urls[:5]:
                result.append({'url': line[1], 'code': line[2], 'size': line[3], 'ip': line[0]})
            return result

        if model == Top5FrequentRequestsWithServerErrorModel:
            """Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой"""
            urls = []
            result = []
            for line in log_to_str():
                splitted = line.split()
                if int(splitted[CONST_CODE]) // 100 == 5:
                    urls.append(splitted[CONST_IP])
            for key, value in Counter(urls).most_common(5):
                result.append({'ip': key, 'number': value})
            return result
