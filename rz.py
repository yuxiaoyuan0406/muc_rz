#!/usr/bin/python3
# import httplib
import urllib3
import json
from urllib.parse import urlencode, urlparse
import os
import time
import sys

default_auth_url: str = "http://192.168.2.231/srun_portal_pc.php?ac_id=1&"
default_ping_count: int = 3
default_user_info_dir: str = '/etc/rz/user.json'
default_post_header_dir: str = '/etc/rz/header.json'
default_ping_test_url: str = 'baidu.com'

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
        'url', default_auth_url)
    # check authorization url
    host: str = urlparse(url).hostname
    assert ping(host, config.get('pingCount', default_ping_count)
                ) == 0, '[ERROR]: Name or service unreachable. Is this host correct?\n{}'.format(host)

    # load user file
    with open(config.get('user', default_user_info_dir), 'r') as _:
        post_body: str = urlencode(json.load(_))
    _.close()

    # load http post header file
    with open(config.get('header', default_post_header_dir), 'r') as _:
        header: dict = json.load(_)
    _.close()

    # create pool manager
    manager: urllib3.poolmanager.PoolManager = urllib3.PoolManager()
    
    # begin checking
    echo('system begin.')
    while (True):
        if(os.system('ping {} -c {} >> /dev/null'.format(
            config.get('pingURL', default_ping_test_url),
            config.get('pingCount', default_ping_count)
        ))):
            # ping failed
            echo('re-connecting...')
            assert ping(host, config.get('pingCount', default_ping_count)
                ) == 0, '[ERROR]: Name or service unreachable.'
            r = post(manager, url, header, post_body)
            echo('response: {}'.format(r.status))
        time.sleep(1)
