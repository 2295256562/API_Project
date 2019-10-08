import copy

import requests
from config.globals import headers
from config.globals import login_url
from functools import lru_cache


class HttpRequest:

    def __init__(self):
        self.headers_teml = {
                        'content-type': 'application/json',
                        'token':None
                       }

    @lru_cache()
    def _login(self):
        """
        :return: 返回token
        """
        data = {
            "username": "",
            "password": ""
        }
        # url = login_url
        # r = requests.post(url=url, json=data, headers=headers)
        x = "ldddwlfwfwelof"
        return x

    def headers(self):
        headers = copy.deepcopy(self.headers_teml)
        headers.update({'token':self._login()})
        return headers


    def http_request(self, url, data, http_method, header):
        """
        http 请求基础类
        :param url: 请求的url
        :param data: 请求数据
        :param http_method: 请求方式  GET、POST
        :return: res
        """
        # headers = self.headers()
        try:
            if http_method.upper() == 'GET':
                res = requests.get(url, data)
            elif http_method.upper() == 'POST':
                res = requests.post(url, data)
            else:
                raise NameError("你输入的请求方式不对， 请你输入GET或POST")
        except Exception as e:
            raise e
        return res


if __name__ == '__main__':
    C = HttpRequest().http_request('http://127.0.0.1:8000/api/reg','{"username":"123425653","password":"1111"}','POST')
    print(C.headers)