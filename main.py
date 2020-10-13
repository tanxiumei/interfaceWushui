# 引入Common、ParamFactory类
from common import Common
from test_excel import ParamFactory
import os


def get_paramAlllineDict():
    # uri_login存储战场的选择武器
    # uri_selectEq = '/selectEq'
    # comm = Common('http://127.0.0.1:12356',api_type='http')
    # 武器编号变量存储武器编号，并且验证返回时是否有参数设计预期结果
    # 获取当前路径绝对值
    curPath = os.path.abspath('.')
    # 定义存储参数的excel文件路径
    searchparamfile = curPath + '\equipmentid_param.xls'
    print(searchparamfile)
    # 调用参数类完成参数读取，返回是一个字典，包含全部的excel数据除去excel的第一行表头说明
    searchparam_dict = ParamFactory().chooseParam('xls', {'file': searchparamfile, 'sheet': 0}).paramAlllineDict()
    print(222222222)
    print(searchparam_dict)
    i = 0
    while i < len(searchparam_dict):
        # 读取通过参数类获取的第i行的参数
        payload = 'equipmentid=' + searchparam_dict[i]['equipmentid']
        print(payload)
        # 读取通过参数类获取的第i行的预期
        exp = searchparam_dict[i]['exp']
        print(exp)
        beizhu = searchparam_dict[i]['备注信息']
        print(beizhu)
        # 进行接口测试
        # response_selectEq = comm.post(uri_selectEq,params=payload)
        # 打印返回结果
        # print('Response内容：' + response_selectEq.text)
        # 读取下一行excel中的数据
        i = i + 1
def get_paramAllline():
    # 获取当前路径绝对值
    curPath = os.path.abspath('.')
    # 定义存储参数的excel文件路径
    searchparamfile = curPath + '\equipmentid_param.xls'
    searchparam_dict = ParamFactory().chooseParam('xls', {'file': searchparamfile, 'sheet': 0}).paramAllline()
    getOneline = ParamFactory().chooseParam('xls', {'file': searchparamfile, 'sheet': 0}).getOneline(4)
    getOneCol = ParamFactory().chooseParam('xls', {'file': searchparamfile, 'sheet': 0}).getOneCol(0)
    paramRowsCount = ParamFactory().chooseParam('xls', {'file': searchparamfile, 'sheet': 0}).paramRowsCount()
    paramColsCount = ParamFactory().chooseParam('xls', {'file': searchparamfile, 'sheet': 0}).paramColsCount()
    paramHeader =ParamFactory().chooseParam('xls', {'file': searchparamfile, 'sheet': 0}).paramHeader()
    paramAlllineDict = ParamFactory().chooseParam('xls', {'file': searchparamfile, 'sheet': 0}).paramAlllineDict()
    print(searchparam_dict)


if __name__ == '__main__':
    import logging

    filename1 = os.path.join(os.getcwd()) + '\log.txt'
    logging.basicConfig(filename=filename1, level=logging.DEBUG)
    logging.debug('this is a message1111')
