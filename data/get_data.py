import string
import urllib
import json
import csv

GOOD_CHARS = string.ascii_letters + string.digits + string.punctuation + ' '

def reverse(text):
    return ''.join(list(reversed(text)))

def split(text, sep=';'):
    auth, quote = reverse(text).split(sep, 1)
    return reverse(auth), reverse(quote)

def get_bad_spot(text):
    for i, char in enumerate(text):
        if char not in GOOD_CHARS:
            return i
    return -1

def clean(text):
    bad_spot = get_bad_spot(text)
    
    if bad_spot == -1:
        return text
    
    else:
        new_text = text[:bad_spot] + text[bad_spot+1:]
        return clean(new_text)

##########

f = urllib.urlopen(
    'https://gist.githubusercontent.com/signed0/d70780518341e1396e11/raw/2a7f4af8d181a714f9d49105ed57fafb3f450960/quotes.json')

res1 = []

for line in f:
    arr = eval(clean(line))
    quote_dict = {
        u'author': unicode(arr[-1]),
        u'quote': unicode(arr[0]),
    }
    res1.append(quote_dict)

f.close()

##########


g = urllib.urlopen(
    'https://raw.githubusercontent.com/4skinSkywalker/Database-Quotes-JSON/master/quotes.json')

text2 = ''
for line in g:
    text2 += line

arr2 = json.loads(text2)

res2 = []
for dict2 in arr2:
    new_dict2 = {
        u'author': unicode(dict2['quoteAuthor']),
        u'quote': unicode(dict2['quoteText']),
    }
    res2.append(new_dict2)

g.close()

##########


k = urllib.urlopen(
    'https://raw.githubusercontent.com/jcalazan/random-quotes/master/db/randomquotes.csv')

res3 = []
for line in k:
    line = clean(line)
    author, quote = split(line)
    quote = quote.strip('"')
    res3.append({
        u'author': unicode(author),
        u'quote': unicode(quote),
    })

res = res1 + res2 + res3

with open(r'data.json', 'w') as z:
    z.write(json.dumps(res, sort_keys=True))
