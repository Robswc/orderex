import requests
from api import secret


def proxy_request(request, ip_guard=None, warn_guard=None, manual_auth=False):
    response = None
    host = secret.proxy['host']
    port = secret.proxy['port']
    if manual_auth:
        print('Enter proxy username:')
        un = input()
        print('Enter proxy password:')
        pw = input()
    else:
        un = secret.proxy['un']
        pw = secret.proxy['pw']

    prx = {'https': str(un) + ':' + str(pw) + '@' + str(host) + ':' + str(port) + '/'}
    if ip_guard:
        ip_guard = secret.ip_whitelist
        response = requests.get('https://api.myip.com', proxies=prx).json()
        if response['ip'] in ip_guard:
            print('Requesting via proxy ({})'.format(response['ip']))
            pass
        else:
            return 'IP ({}) is not on the ip whitelist!\nTerminating Connection'.format(response['ip'])
    if warn_guard is not None:
        pass

    response = requests.get(request, proxies=prx).json()
    return response












