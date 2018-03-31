import collections
import traceback
import requests
import config
import utils
import webob
import json
import sys
import os

def application(environ, start_response):
    # Set up initial parameters and utility instances
    request = webob.Request(environ)
    params = json.loads(request.body) if request.body else {}
    utl = utils.util(environ, start_response)
    res = ''

    try:
        r = requests.get('http://127.0.0.1:9200/quotes/_search', params={'q': 'quote:moon'})
        res = str(r.text)

    except Exception as e:
        res = False
        err_texts = []
        excptn, err_msg, tb = sys.exc_info()
        for file_name, line_no, func_name, text in traceback.extract_tb(tb):
            err_text = '{} (LINE {}) in {}() -> `{}`'.format(
                os.path.basename(file_name), line_no, func_name, text)
            err_texts.append(err_text)
        err_texts.insert(0, '{} {}'.format(e.message, type(e)))
        tb_error = '\n'.join(err_texts)
        res = tb_error

    finally:
        return utl.send_data(res)
