import logging
import os


class Logger:

    def my_log(self, msg, level):
        # 定义日志收集器
        my_log = logging.getLogger('11')
        # 设置级别
        my_log.setLevel('DEBUG')
        # 定义输出格式
        formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')

        # 创建输出渠道
        # 输出到控制台
        conslole = logging.StreamHandler()
        conslole.setLevel('DEBUG')
        conslole.setFormatter(formatter)

        # 输出到日志文件中

        file = logging.FileHandler(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/test_restful/log/' + '1333.log',encoding='UTF-8')
        file.setLevel('DEBUG')
        file.setFormatter(formatter)


        my_log.addHandler(conslole)
        my_log.addHandler(file)

        # 日志收集器
        if level == 'DEBUG':
            my_log.debug(msg)
        elif level == 'INFO':
            my_log.info(msg)
        # 关闭渠道
        my_log.removeHandler(conslole)
        my_log.removeHandler(file)


    def DEBUG(self, msg):
        self.my_log(msg, 'DEBUG')

    def INFO(self, msg):
        self.my_log(msg, 'INFO')

if __name__ == '__main__':
    Logger().DEBUG('WDWSDDSDD')
