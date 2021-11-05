#!/usr/bin/python3
# import httplib
import urllib3
import json
from urllib.parse import urlencode
import os
import time

url = "http://192.168.2.231/srun_portal_pc.php?ac_id=1&"

with open('user.json', 'r') as _:
    post_data = json.load(_)
    post_body = urlencode(post_data)
_.close()

with open('header.json', 'r') as _:
    header = json.load(_)
_.close()

def post(manager, url, headers, body):
    return manager.request(
        method='POST',
        url=url,
        headers=headers,
        body=body
    )

if __name__ == "__main__":
    manager = urllib3.PoolManager()
    while (True):
        if(os.system('ping www.baidu.com -c 3')):
            print('re-connecting...')
            r = post(manager, url, header, post_body)
            print('response: {}'.format(r.status))
        time.sleep(2)
