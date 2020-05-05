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
#df.to_csv('./data/ios.csv', index = False)

social = ["1065781769","1096918571","454638411","284882215","985746746","985746746","1462082664","643496868","304878510","686449807"]
games = ["1344700142","1490384223","1094591345","1499812410","664575829","1498817833","1494449873","623592465","1500564080","406889139"]
health_and_fitness = ["571800810","301521403","387771637","1099771240","634598719","1168348542","462638897","1241229134","300235330","487847188", "1361619409"]
travel = ["293622097","368677368","529379082","401626263","1245772818","904418768","989307692","288113403","336381998","1438670520","474259675","533365777"]
utility = ["868077558","1178765645","416023011","309172177","491126018","926252661","942608209","621574163","1200318119","561625752","917932200"]
education = ["924620788","570060128","756972930","919087726","522826277","552602056","467329677","469863705","875063456","453142230","950424861","546473125","977976646"]
lifestyle = ["429047995","1490078757","680819774","944011620","930441707","1161035371","1222822904","463630399","1462195529","464988855","1288415553","1459289784"]



master_list = [social, games, health_and_fitness, travel, utility, education, lifestyle]
category_dict = {0: "social", 1: "games", 2:"health_and_fitness", 3:"travel", 4:"utility", 5:"education", 6:"lifestyle"}
master_dict = {}
for index, i in enumerate(master_list):
    for j in i:
        master_dict[j] = category_dict[index]


#ios_df = pd.read_csv('./data/ios.csv')
def apply_category(row):
    return master_dict[str(row['appid'])]
df['category'] = df.apply (lambda row: apply_category(row), axis=1)

df.to_csv('./data/ios.csv', index = False)