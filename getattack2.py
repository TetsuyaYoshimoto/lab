#encoding=utf-8

import urllib2
import csv


class SCR:
    def __init__(self):
        self.url = ""


    def geturl(self, url):
        self.url = url

    def ret(self):
        url = "https://job.mynavi.jp/18/pc/search/corp650/outline.html"
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
    a.geturl("https://job.mynavi.jp/18/pc/search/corp" + str(x) + "/outline.html")
    print a.ret()

    with open("output"+ str(x) + "_" + str(x + 2500) + ".csv", "w") as f:
        for i in range(x, x + 2500):
            a.geturl("https://job.mynavi.jp/18/pc/search/corp" + str(i) + "/outline.html")
            html = a.ret()

            try:
                flag1 = html.index("<th scope")
                flag1 = html[flag1:].index("<td class") + flag1
                flag2 = html[flag1:].index("</td>") + flag1
                word2 = html[flag1 + 21:flag2]

                flag1 += 1
                flag1 = html[flag1:].index("<td class") + flag1
                flag2 = html[flag1:].index("</td>") + flag1
                word3 = html[flag1 + 21:flag2]

                flag1 += 1
                flag1 = html[flag1:].index("<td class") + flag1
                flag2 = html[flag1:].index("</td>") + flag1
                word4 = html[flag1 + 21:flag2]

                flag1 += 1
                flag1 = html[flag1:].index("<td class") + flag1
                flag2 = html[flag1:].index("</td>") + flag1
                word5 = html[flag1 + 21:flag2]

                flag1 += 1
                flag1 = html[flag1:].index("<td class") + flag1
                flag2 = html[flag1:].index("</td>") + flag1
                word6 = html[flag1 + 21:flag2]

                flag1 += 1
                flag1 = html[flag1:].index("<td class") + flag1
                flag2 = html[flag1:].index("</td>") + flag1
                word7 = html[flag1 + 21:flag2]

                flag1 += 1
                flag1 = html[flag1:].index("<td class") + flag1
                flag2 = html[flag1:].index("</td>") + flag1
                word8 = html[flag1 + 21:flag2]


                flag1 = html.index("typeId")
                flag1 = html[flag1:].index("typeId")

                flag1 = html[flag1:].index("<h1>") + 4
                flag2 = html[flag1:].index("h1>") + flag1 - 2
                word1 = html[flag1:flag2]

                flag1 = html.index("item") + 25
                word = html[html.index("item") + 6:]
                flag2 = word.index("</div>") + flag1
                word15 = html[flag1: flag2]

                word15 = beau(word15)


                ans.append([word1, word2, word3, word4, word5, word6, word7, word8, word15])
            except :
                pass


       witer = csv.writer(f)
       witer.writerows(ans)


def main()
    sub(950)
    for i in [207475]:
        try:
            sub(i)
            print str(i) + " : OK"
        except:
            print str(i) + " : NO"
            pass


if __name__=="__main__":
    main()

