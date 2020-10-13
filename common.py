import requests
import json


class Common(object):
    def __init__(self,url_base):
        self.url_base = url_base
        self.cookies = self.login()

    def login(self):
        url = self.url_base + "/login/login"
        params = {
            "username": "tanxiumei",
            "password": "111111"

        }
        r = requests.post(url, data=json.dumps(params))
        print(r.cookies)
        # 获取登录时候的cookies，并且把cookies转化成json格式。
        self.cookies = requests.utils.dict_from_cookiejar(r.cookies)
        return self.cookies

    # 封装你自己的get请求，uri是访问路由，params是get请求的参数，类型为字典，如果没有默认为空
    def get(self, uri, params):
        # 拼凑访问地址
        url = self.url_base + uri
        # 通过get请求访问对应地址
        #res = requests.get(url,cookies = self.cookies,params=json.dumps(params))
        res=requests.request("GET", url, params=params, cookies=self.cookies)
        # 返回request的Response结果，类型为requests的Response类型
        return res

    # 封装你自己的post方法，uri是访问路由，params是post请求需要传递的参数，，类型为字典，如果没有参数这里为空
    def post(self, uri, params):
        # 拼凑访问地址
        url = self.url_base+uri
        cookies = self.cookies
        print(cookies)
        if len(params) > 0:
            # 如果有参数，那么通过post方式访问对应的url，并将参数赋值给requests.post默认参数data
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.post(url,cookies = cookies,data=json.dumps(params))
        else:
            # 如果无参数，访问方式如下
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.post(url,cookies = cookies)
        return res
    # 获取用户列表
    def test_getlist_user(self):
        url = "/assign/getUsersLists"
        param = {
        }
        r = self.get(url,param)
        # print(json.dumps(r.json(), indent=2))
        data = r.json()["data"]
        useridlist = []
        for data1 in data:
            useridlist.append(data1["id"])
        print("用户列表：")
        self.useridlist = useridlist
        print(self.useridlist)
        return useridlist

    # 获取站点id列表
    def test_getStationLists(self):
        url = "/station/getStationLists"
        params={}
        r = self.get(url,params)
        print("站点id列表:")
        #print(json.dumps(r.json(),indent=2))#格式化接口返回的内容
        data = r.json()["data"]
        stationidlist = []
        for a in data:
            b = a.get('child', '没有找到该键')
            # print(b)
            for c in b:
                # print(c.get('id', '没有找到该键'))
                stationidlist.append(c.get('id', '没有找到该键'))
        print(stationidlist)
        self.stationidlist = stationidlist
        return stationidlist

    # 派单列表,获取所有派单的id列表dispatchidlist
    def test_getlist_dispatch(self):
        url = "/assign/getAssignPages"
        cur_page = 1#第一页
        idlist = []#总的派单id
        idlist_2 =[]#状态为2，也就是已经审核的id列表
        idlist_1 =[]#状态为1，也就是未审核的id列表
        while True:
            param = {
                "page":cur_page
            }
            r=self.get(url,param)
            # print(json.dumps(r.json(), indent=2))
            #assert r.json()["status"] == 1
            #assert r.json()['msg'] == "ok"
            # print(json.dumps(r.json(),indent=2))
            data = r.json()["data"]["data"]
            last_page = r.json()["data"]["last_page"]
            print("总页数："+str(last_page))
            for data1 in data:
                idlist.append(data1["id"])
                if(data1["status"] == 2):
                    idlist_2.append(data1["id"])
                else:
                    idlist_1.append(data1["id"])
            print(len(idlist))
            if cur_page==last_page:
                break
            cur_page += 1
        #self.dispatchidlist = idlist
        return idlist,idlist_2,idlist_1

    #封装的日志函数
    def get_logger(self):
        import logging
        import logging.handlers
        import datetime

        logger = logging.getLogger('mylogger')
        #设置日志级别，这里设置的是debug，那么debug及以上级别的错误都输出，日志级别从低到高分别是：info、debug、warning、error和critical
        logger.setLevel(logging.DEBUG)
        #用于将日志记录发送到指定的目的位置，并支持日志文件按时间切割
        rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                               atTime=datetime.time(0, 0, 0, 0))
        #用于控制日志信息的最终输出格式
        rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

        f_handler = logging.FileHandler('error.log')
        #设置日志级别
        f_handler.setLevel(logging.INFO)
        f_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

        logger.addHandler(rf_handler)
        logger.addHandler(f_handler)
        return logger
