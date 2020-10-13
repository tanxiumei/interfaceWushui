# FileName : Yaml_read.py
# Author   : tanxiumei
# DateTime : 2020/09/29
# SoftWare : PyCharm

import yaml
import os

# 获取当前文件路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy
from yaml_test.YamlTools import Yaml_tools

filePath = os.path.dirname(__file__)
# print(filePath)
# 获取当前文件的Realpath  D:\WorkSpace\StudyPractice\Python_Yaml\YamlStudy\YamlDemo.py
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
# print(fileNamePath)
# 获取配置文件的路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy\config.yaml
# 构建数据,写入yaml文件
write_data = {
    "cookie1": {
        'domain': '.yiyao.cc',
        'expiry': 1521558688.480118,
        'httpOnly': False,
        'name': '_ui_',
                'path': '/',
                'secure': False,
                'value': 'HSX9fJjjCIImOJoPUkv/QA=='}}
fileNamePath = os.path.join(fileNamePath, 'config.yaml')
yamltool = Yaml_tools(fileNamePath)
data = yamltool.read_data()
#print(data)
yamltool.write_data(write_data)
