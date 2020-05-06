from flask import Flask
from flask import request
import requests
import sys
import io
from lxml import etree
import urllib.parse
import pandas as pd
import json
import pymysql
import datetime
import time

from flask import Blueprint

addId = Blueprint('addId',__name__)

@addId.route('/addId')
def _addId():

        card = request.args.get("card")
        phoneNum = request.args.get("phoneNum")
        operator = request.args.get("operator")
        if(str(phoneNum) == ""):
            phoneNum = "0"
        elif(len(card)<13):
            return('{"Status":200,"Result":"cardLenErr"}')
        elif(str(operator) == ""):
            return('{"Status":200,"Result":"operErr"}')
        else:
            db = pymysql.connect(
            host="cn_sh.jovel.net",
            port=3306,
            user="PhalAPI",
            password='12321Wjwwjw',
            database="PhalAPI",
            charset="utf8")
            cursor = db.cursor()
            unxTime = str(int(time.mktime(datetime.datetime.now().timetuple())))

            cursor.execute("SELECT * FROM cmf_terms_register WHERE card LIKE '%"+ card +"%'")
            tempSql = cursor.fetchone()
            print("success")

            if str(tempSql) != "None":
                    return('{"Status":200,"Result":1,"fullNum":"'+ str(tempSql[3]) +'"}')
            else:
                    cursor.execute("INSERT INTO cmf_terms_register ( name, phone, card, status, he_user_id, he_time ) VALUES ( '人工录入', "+ phoneNum +", '"+ card +"', 1, "+ operator +", "+ unxTime +")")

                    tempSql = cursor.fetchone()
                    print(tempSql)
                    return('{"Status":200,"Result":0}')
