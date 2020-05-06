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
from IdQuery.getId import getId
from IdQuery.addId import addId


app = Flask(__name__)

@app.route('/')
def index():
    return '{"Status":"200"}'

app.register_blueprint(getId)
app.register_blueprint(addId)

if __name__ == '__main__':

    app.run('0.0.0.0', port=80)