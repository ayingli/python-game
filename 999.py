# -*- coding: utf-8 -*-
__author__ = 'ouyangmin'
__time__ = '2021/2/14 23:29'
# 如果该代码不能满足您日常工作需求，可发邮件到liyysap@126.com ，说清楚您的需求，我尽力帮您实现哦

对对对

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

def gethtml(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "It is failed to get html!"

def getcontent(url):
    html = gethtml(url)
    soup = BeautifulSoup(html,"html.parser")
    # print(soup.prettify())
    div = soup.find("div",class_="indent")
    tables = div.find_all("table")

    price = []
    date = []
    nationality = []
    nation = []  #standard
    bookname=[]
    link = []
    score = []
    comment = []
    people = []
    peo = []  #standard
    author = []
    for table in tables:
        bookname.append(table.find_all("a")[1]['title'])   #bookname
        link.append(table.find_all("a")[1]['href'])    #link
        score.append(table.find("span",class_="rating_nums").string)   #score
        comment.append(table.find_all("span")[-1].string)   #comment in a word

        people_info = table.find_all("span")[-2].text
        people.append(re.findall(r'\d+', people_info))  #How many people comment on this book? Note:But there are sublist in the list.

        navistr = (table.find("p").string)   #nationality,author,translator,press,date,price
        infos = str(navistr.split("/"))   #Note this info:The string has been interrupted.
        infostr = str(navistr)            #Note this info:The string has not been interrupted.
        s = infostr.split("/")
        if re.findall(r'\[', s[0]):  # If the first character is "[",match the author.
            w = re.findall(r'\s\D+', s[0])
            author.append(w[0])
        else:
            author.append(s[0])

        #Find all infomations from infos.Just like price,nationality,author,translator,press,date
        price_info = re.findall(r'\d+\.\d+', infos)
        price.append((price_info[0]))   #We can get price.
        date.append(s[-2])  #We can get date.
        nationality_info = re.findall(r'[[](\D)[]]', infos)
        nationality.append(nationality_info)   #We can get nationality.Note:But there are sublist in the list.
    for i in nationality:
        if len(i) == 1:
            nation.append(i[0])
        else:
            nation.append("中")

    for i in people:
        if len(i) == 1:
            peo.append(i[0])

    print(bookname)
    print(author)
    print(nation)
    print(score)
    print(peo)
    print(date)
    print(price)
    print(link)

    # 字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'书名': bookname, '作者': author,'国籍': nation,'评分': score,'评分人数': peo,'出版时间': date,'价格': price,'链接': link,})

    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("C:/Users/zhengyong/Desktop/test.csv", index=False, encoding='utf-8-sig',sep=',')


if __name__ == '__main__':
    url = "https://read.douban.com/ebooks/?dcs=book-nav&dcm=douban"   #If you want to add next pages,you have to alter the code.
    getcontent(url)
