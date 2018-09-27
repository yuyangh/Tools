#!/usr/bin/env python
# coding=utf-8
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}


def check_webpage_existence(url):
    '''
    :param url: url to check existence
    :return: True if url exists False otherwise
    '''
    # with open('/Users/b1ancheng/Desktop/123.txt', 'r') as f:
    #     for line in f:
    # line = line.strip('\n').strip('\ufeff')
    # url = 'http://' + line
    # print(url)
    try:
        response = requests.get(url, headers=headers, timeout=5).status_code
        # print(response)
        if response == 200:
            # print("ok")
            return True
        else:
            # print(response)
            return False
    except Exception as e:
        # with open('/Users/b1ancheng/Desktop/1.txt', 'a+') as f1:
        #     error = f1.write(line + '\n')
        # print(e)
        return False
