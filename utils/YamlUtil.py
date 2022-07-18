
#1 、创建类
import os

import yaml


class YamlReader:
#2、初始化文件是否存在
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise  FileNotFoundError("文件不存在1")
        self._data = None
        self._data_all = None

#3、yaml读取
#单个
    def data(self):
        #第一次调用data 读取yaml文档 如果不是 直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, "rb") as a:
                self._data = yaml.safe_load(a)
        return  self._data

#多个
    def data_all(self):
        #第一次调用data 读取yaml文档 如果不是 直接返回之前保存的数据
        if not self._data_all:
            with open(self.yamlf, "rb") as a:
                self._data_all = list(yaml.safe_load_all(a))
        return  self._data_all