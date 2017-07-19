
#encoding=utf-8

from selenium import webdriver
import time
import csv


class Sharch_data:
    def __init__(self):
        self.url = ""
        self.hpurl = ""
    def _Set_(self, com):
        self.url = "http://www.google.co.jp/search?q=株式会社+" + com + "+決算短信"
        self.driver = webdriver.Chrome("Your web driver full path")

    def _fit_(self):
        try:
            self.driver.get(self.url)
            page_source = self.driver.page_source
            flag = page_source.index("<h3 class=") + 23
            data1 = page_source[flag:flag + 100]
            data1 = data1.split("\"")
            self.hpurl = data1[0]
            self.driver.get(self.hpurl)
            page_source = self.driver.page_source
            self.driver.quit()
            try:
                if page_source.index("決算短信") != 0:
                    return self.hpurl
            except:
                return ""
        except:
            self.driver.quit()
            return ""



def main(low, up):

    f = open("list.csv", "r")
    data = csv.reader(f)
    count = 0

    f1 = open("outlist" + str(low) + "_" + str(up) + ".csv", "w")
    writer = csv.writer(f1, lineterminator = "\n")

    ans = []

    for da in data:
        count += 1
        if count <= low:
            pass
        elif count >= up:
            break
        else:
            try:
                a = Sharch_data()
                print(str(count), str(da[0]))
                a._Set_(str(da[0]))
                url = a._fit_()
                a = None
                if len(url) >= 2:
                    ans.append([str(da[0]), url])
                    print("〇")
                else:
                    print("×")
                    pass
            except: pass

    writer.writerows(ans)
    f.close()

if __name__=="__main__":
    main(17000, 17765)



