import os
import unittest

from public.http_request import HttpRequest
from ddt import ddt, data
from public.do_excel import DoExcel
from public.log import Logger

c = os.path.dirname(os.path.dirname(__file__)) + '/test_data/xxxc.xlsx'
test_data = DoExcel(c, '掘金').get_data()


@ddt
class Test_Request(unittest.TestCase):

    @data(*test_data)
    def test_request(self, item):

        # if item['check_sql'] != None:
        #     # 是否需要执行前置sql
        #     pass


        if item.find
        res = HttpRequest().http_request(item['url'], eval(item['data']), item['method'],item['header(Y/N)'])
        Logger().INFO('请求的地址：{}, 请求方法：{}， 请求参数：{}'.format(item['url'], item['method'], item['data']))
        try:
            # Logger().INFO("断言{}---{}".format(eval(item['expected']), res.json()))
            self.assertEqual(item['expected'], res.json()["userId"])  # 断言
            TestResult = "PASS"
        except AssertionError as e:
            TestResult = "FAIL"
            raise e
        finally:
            DoExcel(c, '掘金').write_back(item['case_id'] + 1, str(res.json()), TestResult)
            dict = {}
            dict = res.json()
            print(dict)
