import unittest

from public.http_request import HttpRequest
from ddt import ddt, data
from public.do_excel import DoExcel
from public.log import Logger

test_data= DoExcel(r'D:\Python代码\API_Project\test_data\xxxc.xlsx', '112').get_data()

@ddt
class Test_Request(unittest.TestCase):

    @data(*test_data)
    def test_request(self, item):

        if item['check_sql'] !=None:
            # 是否需要执行前置sql
            pass


        res = HttpRequest().http_request(item['url'], eval(item['data']), item['method'])
        Logger().INFO('请求的地址：{}, 请求方法：{}， 请求参数：{}'.format(item['url'],item['method'], item['data']))
        try:
            Logger().INFO("断言{}---{}".format(eval(item['expected']), res.json()))
            self.assertEqual(eval(item['expected']), res.json())  # 断言
            TestResult = "PASS"
        except AssertionError as e:
            TestResult = "FAIL"
            raise e
        finally:
            DoExcel(r'D:\Python代码\API_Project\test_data\xxxc.xlsx', '112').write_back(item['case_id']+1, str(res.json()), TestResult)
