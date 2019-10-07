import unittest
import HTMLTestRunnerNew
from test_case.test_http_request import Test_Request

suite = unittest.TestSuite()
loder = unittest.TestLoader()
suite.addTest(loder.loadTestsFromTestCase(Test_Request))

with open('test_restful/html_report/api_test.html', 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        title="单元测试1005",
        description="单元测试1005",
        tester="xiaoxiao"
    )
    runner.run(suite)