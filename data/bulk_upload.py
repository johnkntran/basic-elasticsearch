from pprint import pprint
import json
import csv

with open(r'data.json') as f:
    text = ''
    for line in f:
        text += line
    data = json.loads(text)

def escape_double_quotes(text):
    return text.replace('"', '\"')

with open(r'bulk.json', 'wb') as g:
    for d in data:
        g.write('{ "index": {"_index": "quotes", "_type": "doc"} }\n')
        g.write('< "author": "{}", "quote": "{}" >\n'.format(
            escape_double_quotes(d['author']),
            escape_double_quotes(d['quote']))
                .replace('<', '{').replace('>', '}')
        )
        
