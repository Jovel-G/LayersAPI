from flask import Flask
from flask import request
import requests
import sys
import io
from lxml import etree
import urllib.parse
import json
import pymysql
import datetime
import time

from flask import Blueprint

getId = Blueprint('getId',__name__)

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt

getId = Blueprint('getId',__name__)

@getId.route('/getId')
def _getId():

        shopId = {'2': '利群胶州购物广场', '3': '利群胶州商厦', '4': '北方国贸（原新源）', '5': '西城利群超市', '6': '大润发阜安店', '7': '大润发三里河店', '8': '国货丽达购物中心', '12': '中百佳乐家超市', '13': '龙洲酒业连锁店'}

        card = request.args.get("card")

        db = pymysql.connect(
        host="",
        port=3306,
        user="",
        password='',
        database="",
        charset="utf8")
        cursor = db.cursor()

        cursor.execute("SELECT * FROM cmf_terms_register WHERE card LIKE '%"+ card +"%'")
        tempSql = cursor.fetchone()
        if str(tempSql) != "None":
                cursor.execute("SELECT * FROM cmf_users WHERE id LIKE '%"+ str(tempSql[8]) +"%'")
                userSql = cursor.fetchone()
                return('{"Status":200,"Result":1,"fullNum":"'+ str(tempSql[3]) + " 于 "+ timestamp_datetime(tempSql[9]) +" 时在 "+ shopId[str(tempSql[4])] + " 被管理员 "+ userSql[3] +" 核销" + '"}')
        else:
                return('{"Status":200,"Result":0}')



