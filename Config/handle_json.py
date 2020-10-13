import sys
import os
import configparser
base_path = os.getcwd()
base_path = "D:/testResult/appTestDemo"
sys.path.append(base_path)
import json
def read_json(file_name=None):
    if file_name==None:
        file_path = base_path+"/Config/user_data.json"
    else:
        file_path = base_path+file_name
    with open(file_path,encoding='UTF-8') as f:
        data = json.load(f)
    return data

def get_value(key,file_name=None):
    data = read_json(file_name)
    return data[key]