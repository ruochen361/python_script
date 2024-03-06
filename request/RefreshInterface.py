#!/usr/bin/env python
# coding:utf-8

# -*- coding: utf-8 -*-
import time
import requests
import pandas as pd
import tkinter
import tkinter.messagebox


class Article():
    def __init__(self, url, times,interval):
      self.url = url
      self.times = times
      self.interval = interval


class Visitor(object):
    def __init__(self, article_list):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/73.0.3679.0 Safari/537.36'}
        self.article_list = article_list  # 用于保存所有的文章链接
        self.visitor_count = 0  # 记录已访问次数
#        self.interval = interval # 时间间隔
#        self.threshold = threshold # 刷新阈值

    def visitor(self):
        for article in self.article_list:
            count = 0
            print("\r")
            while count < article.times:
                response = requests.get(url=article.url, headers=self.headers)
                count +=1
                self.visitor_count += 1
                print("\r "+article.url+"访问次数 %s" % count, end='')
                time.sleep(article.interval)
                
    def run(self):
        self.visitor()


def main():
    article_list = build_article_list()  # 需要刷的链接

    visitor = Visitor(article_list)
    visitor.run()
    root = tkinter.Tk
    root.minsize = (300,300)
    tkinter.messagebox.askokcancel(message="刷新完成")


def build_article_list():
    article_list = []  # 需要刷的链接
    df = pd.read_excel('./test.xlsx')
    data_dict = df[df.columns].to_dict(orient='records')
    for d in data_dict: 
#        article_list.append(Article(f"https://m.bkeconomy.com/api/addpv?uuid={d['uuid']}",d['times'],d['interval']))
        article_list.append(Article(f"https://m.bjnews.com.cn/api/addpv?uuid={d['uuid']}",d['times'],d['interval']))
    return article_list


if __name__ == '__main__':
    main()