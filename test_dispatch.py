import json
from json import JSONDecodeError

import requests
import json
from common import Common
import pytest
from test_excel import ParamFactory
import os
import logging
logging.basicConfig(level=logging.DEBUG)
from xlrd import open_workbook
from xlutils.copy import copy

def getdata(num):
    curPath = os.path.abspath('.')
    # 定义存储参数的excel文件路径
    searchparamfile = curPath + r'\equipmentid_param.xls'
    print(searchparamfile)
    # 调用参数类完成参数读取，返回是一个字典，包含全部的excel数据除去excel的第一行表头说明
    paramAllline = ParamFactory().chooseParam(
        'xls', {'file': searchparamfile, 'sheet': num}).paramAllline()
    print(paramAllline)
    return paramAllline
def write_to_excel(row,col,data1):
    print(row)
    r_xls = open_workbook('equipmentid_param.xls')  # 读取excel文件
    row1 = r_xls.sheets()[0].nrows  # 获取已有的行数
    excel = copy(r_xls)  # 将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)  # 获取要操作的sheet

    # 对excel表追加一行内容
    table.write(row,col,data1)  # 括号内分别为行数、列数、内容
    excel.save('equipmentid_param.xls')  # 保存并覆盖文件
distance=2
class TestHttp:
    # 所有用例执行之前只执行一次
    def setup_class(self):
        # 定义一个Common类的实例，获取cookies值
        self.comm = Common("http://61.160.70.70:10001")
        #self.cookies = self.comm.login()
        #self.url_base = "http://61.160.70.70:10001"
        self.dispatchidlist = self.comm.test_getlist_dispatch()[0]  # 所有的派单id列表
        self.dispatchidlist_2 = self.comm.test_getlist_dispatch()[
            1]  # 未被审核的派单id列表
        self.dispatchidlist_1 = self.comm.test_getlist_dispatch()[
            2]  # 已经被审核的派单id列表
        self.useridlist = self.comm.test_getlist_user()  # 用户id列表
        self.stationidlist = self.comm.test_getStationLists()  # 站点列表
        print("派单列表:" + str((self.dispatchidlist)))
        print("派单列表2:" + str((self.dispatchidlist_2)))
        print("派单列表1:" + str((self.dispatchidlist_1)))
        # print(getdata())
        # print(self.useridlist)
        self.logger = self.comm.get_logger()
        self.logger.info('测试用户登录')
        self.cur_row = 2

    # 每个用例执行之前执行一次
    def setup(self):
        pass
    # 每个用例执行之后执行一次

    def test_post(self):
        pass
    # 新增派单

    @pytest.mark.parametrize('list2', getdata(0))
    def test_add_dispatch(self, list2):
        global distance
        print(list2)
        url = list2[5]
        id = self.useridlist[0]
        sid = self.stationidlist[1]
        type = list2[7]
        params = {
            "sid": sid,  # 站点名
            "type": type,  # 运维项目
            "assigner_id": id,
            "content": "维修内容t11111est"  # 维修内容
        }
        try:
            r = self.comm.post(url, params)
            print(json.dumps(r.json(), indent=2))
            assert r.json()["status"] == 1
            print(r.json()["msg"])
            print("测试通过呀！")
            self.logger.info('新增派单成功，新增的id为：')
            self.logger.info(id)
            write_to_excel(distance,10,"测试通过")
            distance+=1
            print("哈哈哈哈："+str(distance))
        except JSONDecodeError:
            print("程序出现了异常哦！")
            print("测试不通过呀")
            self.logger.debug('新增派单出错，错误信息：')
            write_to_excel(distance, 10, "测试不通过")
            distance += 1

    # 删除派单
    def test_del_dispatch(self):
        url = "/assign/deleteAssign"
        id = self.dispatchidlist[1]
        param = {
            "id": id,
            "type": 0
        }
        #id1 = len(self.dispatchidlist)
        r = self.comm.post(url, param)
        print(json.dumps(r.json(), indent=2))
        #id2 = len(self.dispatchidlist)
        assert r.json()["status"] == 1
        #assert id1 == id2+1
    # 派单详情
    @pytest.mark.parametrize('list1', getdata(1))
    def test_detail_dispatch(self, list1):
        url = list1[0]
        if(list1[1] == 'dispatchidlist[2]'):
            id = self.dispatchidlist[2]
        else:
            id = int(list1[1])
        param = {
            "id": id
        }
        try:
            r = self.comm.get(url, param)
            print(r.json()["data"]["id"])
            tempid = r.json()["data"]["id"]
            assert r.json()['status'] == 1
            assert r.json()["msg"] == "ok"
        except BaseException:
            r = self.comm.get(url, param)
            print(r.json())
            print("参数出错")

    # 派单审核功能
    def test_check_diapatch(self):
        print("派单id列表：" + str(self.dispatchidlist_1[0]))
        url = "/assign/checkAssign"
        param = {
            "id": self.dispatchidlist_1[0],
            "status": 2
        }
        r = self.comm.post(url, param)
        print(r.json())
