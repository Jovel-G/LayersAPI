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

query = Blueprint('query',__name__)

@query.route('/query')
def _query():

        card = request.args.get("card")

        db = pymysql.connect(
        host="qdm768868121.my3w.com",
        port=3306,
        user="qdm768868121",
        password='Jiaozhou365',
        database="qdm768868121_db",
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

