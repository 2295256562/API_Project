import re
import requests

# 解析字符串中全局变量并进行替换
def resolve_global_var(pre_resolve_var, global_var_dic, global_var_regex='\${.*?}',
                       match2key_sub_string_start_index=2, match2key_sub_string_end_index=-1):
    """
    :param pre_resolve_var: 准备进行解析的变量<str>
    :param global_var_dic: 全局变量字典<dict>
    :param global_var_regex: 识别全局变量正则表达式<str>
    :param match2key_sub_string_start_index: 全局变量表达式截取成全局变量字典key值字符串的开始索引<int>
    :param match2key_sub_string_end_index: 全局变量表达式截取成全局变量字典key值字符串的结束索引<int>
    :return: 解析后的变量<str>
    """

    if not isinstance(pre_resolve_var, str):
        raise TypeError('pre_resolve_var must be str！')

    if not isinstance(global_var_dic, dict):
        raise TypeError('global_var_dic must be dict！')

    if not isinstance(global_var_regex, str):
        raise TypeError('global_var_regex must be str！')

    if not isinstance(match2key_sub_string_start_index, int):
        raise TypeError('match2key_sub_string_start_index must be int！')

    if not isinstance(match2key_sub_string_end_index, int):
        raise TypeError('match2key_sub_string_end_index must be int！')

    re_global_var = re.compile(global_var_regex)

    def global_var_repl(match_obj):
        start_index = match2key_sub_string_start_index
        end_index = match2key_sub_string_end_index
        match_value = global_var_dic.get(match_obj.group()[start_index:end_index])
        return match_value if match_value else match_obj.group()

    resolved_var = re.sub(pattern=re_global_var, string=pre_resolve_var, repl=global_var_repl)
    return resolved_var


if __name__ == '__main__':

    # pre_resolve_var = 'left status right, left ${data} right'  # 需要解析的变量
    # global_var_dic = {'status': 'ccc', 'data': 'UPC'}          # 全局变量字典
    # resolved_str = resolve_global_var(pre_resolve_var=pre_resolve_var, global_var_dic=global_var_dic)
    # print(resolved_str)

    pre_resolve_var = 'https://post-storage-api-ms.juejin.im/v1/getDetailData?uid=${username}&device_id=1570520905829&token=${token}&src=web&type=entry&postId=5cc11f6be51d45401f566d14'  # 需要解析的变量
    global_var_dic = {'user': "111",'role': 'guest', 'username': 'yuanman99', 'selfDescription': '',
                               'email': '', 'mobilePhoneNumber': '17671105406', 'jobTitle': '',
                               'company': '', 'avatarHd': '', 'avatarLarge': '', 'blogAddress': '',
                               'deviceType': 'web', 'editorType': 'markdown', 'juejinPower': 0, 'level': 0,
                               'rankIndex': 0, 'roles': None, 'allowNotification': True, 'emailVerified': False,
                               'mobilePhoneVerified': True, 'isAuthor': False, 'isUnitedAuthor': False, 'blacklist': False,
                               'followeesCount': 0, 'followersCount': 0, 'postedPostsCount': 0, 'postedEntriesCount': 0,
                               'collectedEntriesCount': 0, 'viewedEntriesCount': 2, 'totalViewsCount': 0, 'subscribedTagsCount': 0,
                               'totalCollectionsCount': 0, 'totalHotIndex': 0, 'totalCommentsCount': 0, 'collectionSetCount': 0,
                               'latestLoginedInAt': '2019-10-09T02:34:22.962Z', 'createdAt': '2019-10-08T07:47:54.243Z', 'updatedAt':
                                   '2019-10-09T02:34:22.962Z', 'useLeancloudPwd': False, 'community': None, 'objectId': '5d9c3f2af265da5bb55837f9',
                               'uid': '5d9c3f2af265da5bb55837f9',
                      'token': 'eyJhY2Nlc3NfdG9rZW4iOiJ0SkZQdXZTYjBpV21LMTA4IiwicmVmcmVzaF90b2tlbiI6IlV4b2EzV3d1R0pQd2p4N0YiLCJ0b2tlbl90eXBlIjoibWFjIiwiZXhwaXJlX2luIjoyNTkyMDAwfQ==',
                      'clientId': 1570588415469, 'userId': '5d9c3f2af265da5bb55837f9'} # 全局变量字典
    resolved_str = resolve_global_var(pre_resolve_var=pre_resolve_var, global_var_dic=global_var_dic)
    print(resolved_str)

    # data = {
    #     "usernmae": "12345678901",
    #     "userpassword": "123456",
    # }
    # res = requests.post(url='http://auth.dlab.com/cas/login',data=data)
    # # print(res.json())
    #
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    #     "token": None
    # }
    #
    # global_var_dic = {'token': str(res.json()['msg'])}
    # pre_resolve_var ='AAAA'
    # # print(headers['token'])
    # str = resolve_global_var(pre_resolve_var, global_var_dic)
    # headers.update({'token':str})
    # print(headers)





