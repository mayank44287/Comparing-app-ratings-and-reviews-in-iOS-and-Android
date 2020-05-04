import pandas as pd
import ast
import json
import re
from itertools import chain



json_list = []
with open('./data/ios_data.json',encoding='utf-8', errors='ignore') as json_file:
    string_json =  '[' + json_file.read() + ']'
    #print(string_json)
    x = eval(string_json.replace(']', '],')) 
    #print(json_file.read().replace(']', '],'))

for i in x[0]:
    for j in i:
        review_entry = json.loads(j)
        p = re.compile("\?id=([a-z0-9\-]+)\&?")
        result = p.search(review_entry['url'])
        appid = result.group(1)
        review_entry['appid'] = appid
        json_list.append(review_entry)


df = pd.DataFrame(json_list)
df.to_csv('./data/ios.csv', index = False)