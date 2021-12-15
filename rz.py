#!/usr/bin/python3
# import httplib
import urllib3
import json
from urllib.parse import urlencode, urlparse
import os
import time
import sys


def post(
        manager: urllib3.poolmanager.PoolManager,
        url: str,
        headers: dict,
        body: str):
    '''
    fire a post
    '''
    return manager.request(
        method='POST',
        url=url,
        headers=headers,
        body=body
    )


def ping(host: str, count: int):
    '''
    ping a host for limited times
    '''
    return os.system('ping {} -c {} >> /dev/null'.format(
        host, count
    ))
    
def echo(msg: str):
    '''
    calling system function echo
    '''
    return os.system('echo \"{}\"'.format(msg))


if __name__ == "__main__":
    # check for config file
    assert len(sys.argv) >= 2, '[ERROR]: No config file. val = {}'.format(
        len(sys.argv))

    # load config file
    with open(sys.argv[1], 'r') as _:
        config: dict = json.load(_)
    _.close()

    # get authorization url
    url: str = config.get(
        'url', "http://192.168.2.231/srun_portal_pc.php?ac_id=1&")
    # check authorization url
    host: str = urlparse(url).hostname
    assert ping(host, config.get('pingCount', 3)
                ) == 0, '[ERROR]: Name or service unreachable. Is this host correct?\n{}'.format(host)

    # load user file
    with open(config.get('user', '/etc/rz/user.json'), 'r') as _:
        post_body: str = urlencode(json.load(_))
    _.close()

    # load http post header file
    with open(config.get('header', '/etc/rz/header.json'), 'r') as _:
        header: dict = json.load(_)
    _.close()

    manager: urllib3.poolmanager.PoolManager = urllib3.PoolManager()
    echo('system begin.')
    while (True):
        if(os.system('ping {} -c {} >> /dev/null'.format(
            config.get('pingURL', 'baidu.com'),
            config.get('pingCount', 3)
        ))):
            echo('re-connecting...')
            assert ping(host, config.get('pingCount', 1)
                ) == 0, '[ERROR]: Name or service unreachable.'
            r = post(manager, url, header, post_body)
            echo('response: {}'.format(r.status))
        time.sleep(1)
