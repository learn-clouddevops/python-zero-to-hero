import random
import array
import os
import shutil
import json
import csv
from datetime import datetime,timedelta
import time
import re

print(random.randint(1, 10))
print(random.choice(['apple', 'banana', 'cherry']))

print(os.getcwd())

shutil.copyfile('sorce.txt', 'destination.txt')

#data serialization
data    = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print   (type(data)) #dict
json_data = json.dumps(data)
print(type  (json_data))

parsed_data = json.loads(json_data)
print(type(parsed_data)) #desrialaze it


with open('example.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])


with open('example.csv', mode='r') as file:
    reader= csv.reader  (file)
    for row in reader:
        print   (row)  

now = datetime.now()
print(now)
yesterday = now-timedelta(days=1)
print(yesterday)

#time
print(time.time())

time.sleep(2)
print(time.time())


#regular expression
pattern = r'\d+'
text = "There are 123 apples and 456 oranges."
matches = re.search(pattern, text)
print(matches.group())
