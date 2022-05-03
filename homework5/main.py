import json
import pathlib
from collections import Counter
import argparse

IP = 0
TYPE = 5
URL = 6
CODE = 8
SIZE = 9

TITLE1 = "Общее количество запросов"
TITLE2 = "Общее количество запросов по типу"
TITLE3 = "Топ 10 самых частых запросов"
TITLE4 = "Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой"
TITLE5 = "Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой"

json_structure = []


parser = argparse.ArgumentParser()
parser.add_argument("--json", help="сохранение данных в JSON", action="store_true")
args = parser.parse_args()


def log_to_str():
    dir_path = pathlib.Path.cwd()
    file_path = (pathlib.Path(dir_path, 'access.log'))
    with open(file_path) as file:
        for line in file:
            yield line


def save_log(log_srting):
    if not args.json:
        dir_path = pathlib.Path.cwd()
        file_path = (pathlib.Path(dir_path, 'python_result.log'))
        with open(file_path, "a") as file:
            file.write(str(log_srting))
            file.write('\n')


def save_json():
    if args.json:
        dir_path = pathlib.Path.cwd()
        file_path = (pathlib.Path(dir_path, 'python_result.json'))
        with open(file_path, "a") as file:
            file.write(json.dumps(json_structure))


save_log(TITLE1)
n = 0
for _ in log_to_str():
    n += 1
save_log(n)
json_structure.append({TITLE1: n})

save_log('\n' + TITLE2)
urls2 = []
json2 = []
for line in log_to_str():
    urls2.append(line.split()[TYPE][1::])
for key, value in Counter(urls2).most_common():
    save_log(str(value) + ' - ' + key)
    json2.append({key: value})
json_structure.append({TITLE2: json2})

save_log('\n' + TITLE3)
urls3 = []
json3 = []
for line in log_to_str():
    urls3.append(line.split()[URL])
for key, value in Counter(urls3).most_common(10):
    save_log(str(value) + ' ' + key)
    json3.append({key: value})
json_structure.append({TITLE3: json3})

save_log('\n' + TITLE4)
urls4 = []
json4 = []
for line in log_to_str():
    splitted = line.split()
    if int(splitted[CODE]) // 100 == 4:
        urls4.append([splitted[IP], splitted[URL], splitted[CODE], splitted[SIZE]])
urls4 = sorted(urls4, key=lambda tup: int(tup[3]), reverse=True)
for line in urls4[:5]:
    arg = line[3] + ' ' + line[0] + ' ' + line[2] + ' ' + line[1]
    save_log(line[3] + ' ' + line[0] + ' ' + line[2] + ' ' + line[1])
    json4.append({'IP': line[0], 'URL': line[1], 'CODE': line[2], 'SIZE': line[3]})
json_structure.append({TITLE4: json4})

save_log('\n' + TITLE5)
urls5 = []
json5 = []
for line in log_to_str():
    splitted = line.split()
    if int(splitted[CODE]) // 100 == 5:
        urls5.append(splitted[IP])
for key, value in Counter(urls5).most_common(5):
    save_log(str(value) + ' ' + key)
    json5.append({key: value})
json_structure.append({TITLE5: json5})

save_json()
