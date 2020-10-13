import yaml
import os

class Yaml_tools():
    def __init__(self,fileNamePath):
        self.yamlPath = fileNamePath
    #定义读取yaml文件的函数
    def read_data(self):
        # 加上 ,encoding='utf-8'，处理配置文件中含中文出现乱码的情况。
        f = open(self.yamlPath, 'r', encoding='utf-8')
        cont = f.read()
        x_data = yaml.load(cont, Loader=yaml.FullLoader)
        return(x_data)
    #定义写入yaml文件的函数
    def write_data(self,data):
        # 写入yaml 文件
        # a 追加写入，w,覆盖写入
        fw = open(self.yamlPath, 'a', encoding='utf-8')
        # data = {'domain': '.yiyao.cc', 'expiry': 1521558688.480118}
        # 装载数据
        yaml.dump(data, fw)
        # 读取数据，获取文件
        f = open(self.yamlPath, 'r', encoding='utf-8')
        # 读取文件
        cont = f.read()
        # 加载数据
        x = yaml.load(cont, Loader=yaml.FullLoader)
        # 打印数据
        #print(x)
        # 打印读取写入的数据
        print(x.get("cookie1"))
