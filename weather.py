import requests
from bs4 import BeautifulSoup
import csv


def get_url(city_name):
    url = 'http://www.weather.com.cn/weather/'
    with open('city.txt' , 'r' , encoding='utf-8') as fs:
        lines = fs.readlines:
        if (city_name in line):
            code = line.split('=')[0].strip()
            return url + code + '.shtml'
    raise ValueError('invalid city name')


def get_content(url , data=None):
    try:
        r = requests.get(url , timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.txt
    except:
        return '产生异常'


def get_data(html , city)
    https: // blog.csdn.net / qq_40958485 / article / details / 85067636