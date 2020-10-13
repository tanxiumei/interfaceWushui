import datetime

from xlrd import open_workbook
from xlutils.copy import copy
import os

from test_excel import ParamFactory

# r_xls = open_workbook('equipmentid_param.xls')  # 读取excel文件
# row = r_xls.sheets()[0].nrows  # 获取已有的行数
# excel = copy(r_xls)  # 将xlrd的对象转化为xlwt的对象
# table = excel.get_sheet(0)  # 获取要操作的sheet
#
# # 对excel表追加一行内容
# table.write(5, 10, '内容1')  # 括号内分别为行数、列数、内容
#
# excel.save('equipmentid_param.xls')  # 保存并覆盖文件

datetime.datetime.strptime(string,'%Y-%m-%d %H:%M:%S')