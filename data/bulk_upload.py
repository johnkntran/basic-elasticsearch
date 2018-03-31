from pprint import pprint
import json
import csv

with open(r'data.json') as f:
    text = ''
    for line in f:
        text += line
    data = json.loads(text)

with open(r'bulk.json', 'wb') as g:
    for d in data:
        g.write('{ "index": {"_index": "quotes", "_type": "doc"} }\n')
        g.write('< "author": {}, "quote": {} >\n'.format(d['author'], d['quote']).replace('<', '{').replace('>', '}'))
        
