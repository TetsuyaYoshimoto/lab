#encoding=utf-8

import urllib2


class SCR:
    def __init__(self):
        self.url = ""


    def geturl(self, url):
        self.url = url

    def ret(self):
        proxy = {"http":"http://chache.ccs.kogakuin.ac.jp:8080/",
                 "https":"https://cache.ccs.kogakuin.ac.jp:8080/"}
        proxy_handler = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        fp = urllib2.urlopen(self.url)
        html = fp.read()
        fp.close()
        return html


def beau(word):
    reword = ""
    word = map(str, word.split())
    for wo in word:
        reword+=wo
    return reword


def sub(): 
    ans = []
    a = SCR()
    a.geturl("http://s.weibo.com/weibo/Japan&b=2&page=1")
    html = a.ret()

    f = open("test.txt", "w")
    f.write(html)
    f.close()


def main():
    sub()


if __name__=="__main__":
    main()


