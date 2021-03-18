
import socket

import requests


def get_ip():
    """
    查询对外ip地址
    :return: ip
    """
    url = r'http://www.3322.org/dyndns/getip'
    r = requests.get(url)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    # print(ip)
    return ip


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


if __name__ == '__main__':
    print(get_ip())
    IP = get_ip()
    print(IP)
    if IP == '120.0.0.1':
        MYSQL_HOST = '10.0.0.1'
    else:
        MYSQL_HOST = '120.0.0.1'
    print(MYSQL_HOST)
    print(get_host_ip())
