import sys
import os
import configparser

from Config.handle_json import get_value

#base_path = os.getcwd()
base_path = "D:/testResult/appTestDemo"
sys.path.append(base_path)
import json

print(get_value("api3/getver2", "/Config/code_message.json"))
