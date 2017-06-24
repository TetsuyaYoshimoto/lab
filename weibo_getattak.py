#encoding=utf-8

import urllib2

class SCR:
    def __init__(self):
        self.url = ""

    def seturl(self, url):
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

def main():
    ans = []
    #make instans name "a"
    a = SCR()
    #"a" instans have self.url. setlurl func effective chainge "a" instans in url value.
    a.seturl("http://s.weibo.com/weibo/Japan&b=2&page=1")
    #"a" instans have htmldata. ret func return html on seturl
    html = a.ret()

    #save step
    f = open("test.txt", "w")
    f.write(html)
    f.close()

if __name__=="__main__":
    main()
