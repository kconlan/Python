#Kevin Conlan Python 6651-01 Professor Nurmatova Web Crawler

import urllib.request
from urllib.error import  URLError
import re


def url_visit(url, domain):
    global backlog_crawler
    if( len( backlog_crawler )>100):
        return
    if(url in backlog_crawler and backlog_crawler[url] == 1):
        return
    else:
        backlog_crawler[url] = 1
        print("Processing:", url)
    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")
            regexp_title = re.compile('<title>(?P<title>(.*))</title>')
            regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
            regexp_pagetype = re.compile('<meta name="pagetype" content="(?P<pagetype>(.*))" />')
            regexp_url = re.compile("http://"+domain+"[/\w+]*")

            result = regexp_title.search(content_string, re.IGNORECASE)

            if result:
                title = result.group("title")
                print(title)

            result = regexp_keywords.search(content_string, re.IGNORECASE)

            if result:
                keywords = result.group("keywords")
                print(keywords)

            result = regexp_pagetype.search(content_string, re.IGNORECASE)

            if result:
                pagetype = result.group("pagetype")
                print(pagetype)

            for (urls) in re.findall(regexp_url, content_string):
                    if(urls  not in backlog_crawler or backlog_crawler[urls] != 1):
                        backlog_crawler[urls] = 0
                        visit_url(urls, domain)
    except URLError as e:
        print("error")

backlog_crawler = {}

seed = "http://www.newhaven.edu/"

backlog_crawler[seed]=0

visit_url(seed, "www.newhaven.edu")
