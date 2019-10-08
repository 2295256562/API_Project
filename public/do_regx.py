import re
from public.get_data import GetData

class DoRegx:

    """
    正则替换类
    """

    @staticmethod
    def do_regx(string):
        """
        :param str:  传入字符
        :return:
        """
        while re.search('\$\{(.*?)\}',string):
            key = re.search('\$\{(.*?)\}',string).group(0)
            value = re.search('\$\{(.*?)\}',string).group(1)
            string =string.replace(key, str(getattr(GetData,value)))
        return string


# s = '{"username":"123425653","password":"${tel_1}"}'
# res = DoRegx.do_regx(s)
#
# print(res)