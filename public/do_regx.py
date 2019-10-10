import re
from public.get_data import GetData

class DoRegx:

    """
    正则替换类
    """
    # 需要传进来的格式为 case_id + 字典或者列表
    # 1.user[tel]   代表取第一个第一个list中的字典user的tel的值
    @staticmethod
    def do_regx(string, dict):
        """
        :param str:  传入字符
        :return:
        """
        # s = zhi.split('.')
        # n = int(s[0])-1
        # data = dict[n]
        #
        # t = s[1]
        # token = dict[n]
        # print(type(token))

        #  对传进来的string 进行切片

        # for i in dict:
        #     print(i)
        while re.search('\$\{(.*?)\}',string):
            key = re.search('\$\{(.*?)\}',string).group(0)
            value = re.search('\$\{(.*?)\}',string).group(1)
            n = value.split('.')

            tmp = dict[int(n[0]) - 1]
            # print(tmp)
            for i in n:
                tmp = tmp[i]
            # print("222222")
            # print("11111",tmp)

            # print(n)
            # for c in dict[n].values():
            #     j = (c[c])


            # for c in dict.values():
            #     f = (c['user'][value])
            string =string.replace(key, tmp)
        return string

# v = [{'1': {'user': {'role': 'guest', 'tel_1': 'yuanman99', 'selfDescription': '',
#                    'email': '', 'mobilePhoneNumber': '17671105406', 'jobTitle':
#                        '', 'company': '', 'avatarHd': '', 'avatarLarge': '',
#                    'blogAddress': '', 'deviceType': 'web', 'editorType':
#                        'markdown', 'juejinPower': 0, 'level': 0, 'rankIndex': 0,
#                    'roles': None, 'allowNotification': True,
#                    'emailVerified': False, 'mobilePhoneVerified': True,
#                    'isAuthor': False, 'isUnitedAuthor': False,
#                    'blacklist': False, 'followeesCount': 0, 'followersCount': 0,
#                    'postedPostsCount': 0, 'postedEntriesCount': 0,
#                    'collectedEntriesCount': 0, 'viewedEntriesCount': 7,
#                    'totalViewsCount': 0, 'subscribedTagsCount': 0, 'totalCollectionsCount': 0,
#                    'totalHotIndex': 0, 'totalCommentsCount': 0, 'collectionSetCount': 0,
#                    'latestLoginedInAt': '2019-10-09T07:37:01.424Z', 'createdAt': '2019-10-08T07:47:54.243Z',
#                    'updatedAt': '2019-10-09T07:37:01.424Z', 'useLeancloudPwd': False,
#                    'community': None, 'objectId': '5d9c3f2af265da5bb55837f9', 'uid': '5d9c3f2af265da5bb55837f9'},
#           'token': 'eyJhY2Nlc3NfdG9rZW4iOiJPU3hrMHlJekpUNHpJemhwIiwi'
#                    'cmVmcmVzaF90b2tlbiI6InlGdnZKU29QNUJIOEs1Y3QiLCJ0'
#                    'b2tlbl90eXBlIjoibWFjIiwiZXhwaXJlX2luIjoyNTkyMDAwfQ==',
#           'clientId': 1570606621409, 'userId': '5d9c3f2af265da5bb55837f9'}},
#      {'2': {'user': {'role': 'guest', 'tel_1': 'yuanman99', 'selfDescription': '',
#                    'email': '', 'mobilePhoneNumber': '17671105406', 'jobTitle':
#                        '', 'company': '', 'avatarHd': '', 'avatarLarge': '',
#                    'blogAddress': '', 'deviceType': 'web', 'editorType':
#                        'markdown', 'juejinPower': 0, 'level': 0, 'rankIndex': 0,
#                    'roles': None, 'allowNotification': True,
#                    'emailVerified': False, 'mobilePhoneVerified': True,
#                    'isAuthor': False, 'isUnitedAuthor': False,
#                    'blacklist': False, 'followeesCount': 0, 'followersCount': 0,
#                    'postedPostsCount': 0, 'postedEntriesCount': 0,
#                    'collectedEntriesCount': 0, 'viewedEntriesCount': 7,
#                    'totalViewsCount': 0, 'subscribedTagsCount': 0, 'totalCollectionsCount': 0,
#                    'totalHotIndex': 0, 'totalCommentsCount': 0, 'collectionSetCount': 0,
#                    'latestLoginedInAt': '2019-10-09T07:37:01.424Z', 'createdAt': '2019-10-08T07:47:54.243Z',
#                    'updatedAt': '2019-10-09T07:37:01.424Z', 'useLeancloudPwd': False,
#                    'community': None, 'objectId': '5d9c3f2af265da5bb55837f9', 'uid': '5d9c3f2af265da5bb55837f9'},
#           'token': 'eyJhY2Nlc3NfdG9rZW4iOiJPU3hrMHlJekpUNHpJemhwIiwi'
#                    'cmVmcmVzaF90b2tlbiI6InlGdnZKU29QNUJIOEs1Y3QiLCJ0'
#                    'b2tlbl90eXBlIjoibWFjIiwiZXhwaXJlX2luIjoyNTkyMDAwfQ==',
#           'clientId': 1570606621409, 'userId': '5d9c3f2af265da5bb55837f9'}}
#      ]
# s = '12123123%ccc=${2.token}&ccc=${2.user.role}'
# z = '2.token'
# res = DoRegx.do_regx(s,v)
# print(res)
#
#
#
#
# c = {1: {'user': {'role': 'guest', 'username': 'yuanman99', 'selfDescription': '', 'email': '', 'mobilePhoneNumber': '17671105406', 'jobTitle': '', 'company': '', 'avatarHd': '', 'avatarLarge': '', 'blogAddress': '', 'deviceType': 'web', 'editorType': 'markdown', 'juejinPower': 0, 'level': 0, 'rankIndex': 0, 'roles': None, 'allowNotification': True, 'emailVerified': False, 'mobilePhoneVerified': True, 'isAuthor': False, 'isUnitedAuthor': False, 'blacklist': False, 'followeesCount': 0, 'followersCount': 0, 'postedPostsCount': 0, 'postedEntriesCount': 0, 'collectedEntriesCount': 0, 'viewedEntriesCount': 7, 'totalViewsCount': 0, 'subscribedTagsCount': 0, 'totalCollectionsCount': 0, 'totalHotIndex': 0, 'totalCommentsCount': 0, 'collectionSetCount': 0, 'latestLoginedInAt': '2019-10-09T07:37:01.424Z', 'createdAt': '2019-10-08T07:47:54.243Z', 'updatedAt': '2019-10-09T07:37:01.424Z', 'useLeancloudPwd': False, 'community': None, 'objectId': '5d9c3f2af265da5bb55837f9', 'uid': '5d9c3f2af265da5bb55837f9'}, 'token': 'eyJhY2Nlc3NfdG9rZW4iOiJPU3hrMHlJekpUNHpJemhwIiwicmVmcmVzaF90b2tlbiI6InlGdnZKU29QNUJIOEs1Y3QiLCJ0b2tlbl90eXBlIjoibWFjIiwiZXhwaXJlX2luIjoyNTkyMDAwfQ==', 'clientId': 1570606621409, 'userId': '5d9c3f2af265da5bb55837f9'}}
# print(type(c))