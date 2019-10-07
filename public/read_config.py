import configparser


class ReadConfig:
    """
    读取配置文件
    """

    @staticmethod
    def get_config(file_name, section, option):
        """
        获取配置文件
        :param file_name:  路径
        :param section:
        :param option:
        :return:
        """
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf[section][option]
