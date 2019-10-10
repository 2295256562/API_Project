import os
import unittest

from public.http_request import HttpRequest
from ddt import ddt, data
from public.do_excel import DoExcel
from public.log import Logger
from untils.do_gloabs import resolve_global_var
from test_case import test
from public.do_regx import DoRegx

c = os.path.dirname(os.path.dirname(__file__)) + '/test_data/xxxc.xlsx'
test_data = DoExcel(c, '掘金').get_data()


@ddt
class Test_Requests(unittest.TestCase):
    datas = []

    @data(*test_data)
    def test_request(self, item):

        # if item['check_sql'] != None:
        #     # 是否需要执行前置sql
        #     pass

        # global_var_dic = open('test.py', 'r')
        # c = global_var_dic.read()
        # global_var_dic.close()
        # print(c)
        # print(type(eval(c)))
        # url = resolve_global_var(item['url'], eval(c))
        # print(url)

        # 判断url中是否有变量符,如果有就去替换
        url = DoRegx.do_regx(item['url'], self.datas)

        # 判断url是否等于空
        if item['data'] != None:
            data = DoRegx.do_regx(item['data'], self.datas)
        else:
            data = None
        request_data = data

        res = HttpRequest().http_request(url, request_data, item['method'], item['header(Y/N)'])
        Logger().INFO('请求的地址：{}, 请求方法：{}， 请求参数：{}'.format(item['url'], item['method'], item['data']))
        try:
            # Logger().INFO("断言{}---{}".format(item['expected'], res.json()))
            self.assertEqual(item['expected'], res.json()["userId"])  # 断言
            TestResult = "PASS"
        except AssertionError as e:
            TestResult = "FAIL"
            raise e
        finally:
            DoExcel(c, '掘金').write_back(item['case_id'] + 1, str(res.json()), TestResult)
            dict = {}
            key = item['case_id']
            dict[key] = res.json()

            print(dict)
            # dict = res.json()
            # a = open('test.py', 'w')
            # a.write(str(dict))
            # a.close()
