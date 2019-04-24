#-*- coding:utf-8 -*-


import urllib
import re
import requests
import sys
import pymysql

url_name = []

def get():
    hd = {}
    url = 'URL'
    html = requests.get(url,headers = hd).text
    url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)',re.S)
    url_contents = re.findall(url_content,html)

    for i in url_content:
        url_reg = r'data-mp4="(.*?)"'
        url_items = re.findall(url_reg,i)
        if url_items:
            name_reg = re.compile(r'<a href="/detail-.{8}?.html">(.*?)</a>',re.S)
            name_itmes = re.findall(name_reg,i)
            for i,k in zip(name_itmes,url_items):
                url_name.append([i,k])
                print(i,k)
    for i in url_name:
        urllib.urlretrieve(i[1],'video\\%s.mp4'%(i[0].decode('utf-8')))





if __name__ == "__main":
    get()