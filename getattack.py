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


def sub(x): 
    ans = []
    a = SCR()
    a.geturl("https://job.mynavi.jp/18/pc/search/corp" + str(x) + "/employment.html")
    try:
        html = a.ret()
    except:
        try:
            html = a.ret()
        except:
            pass
    if len(html) >= 5600:
        f = open(str(x) + "_1.txt", "w")
        f.write(html)
        f.close()
    else: pass


def main():
    for i in [86369]:
        print i
        try:
            sub(i)
        except:
            try:
                sub(i)
            except:
                try:
                    sub(i)
                except:
                    pass


if __name__=="__main__":
    main()


