from hashlib import md5
import json

file_way = r'way_file\country_url.json'

with open(file_way, 'r', encoding='utf-8') as file:
    dirty_file = json.load(file)

def file(dirty_file):
    account = 0
    while account < len(dirty_file):
        yield dirty_file[account]
        account += 1

for string in file(dirty_file):
    hash_string = md5(str(string).encode()).hexdigest()
    print(hash_string)



