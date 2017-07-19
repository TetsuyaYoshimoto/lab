
#encoding=utf-8

from selenium import webdriver
import time
import csv


class Sharch_data:

    def __init__(self):
        self.driver = None
        self.url = ""

    def _Set_(self, url):
        self.url = url
        self.driver = webdriver.Chrome("/mnt/c/Users/yt/Documents/progrum/lab/attack/chromedriver.exe")

    def _fit_(self):
        self.driver.get(self.url)
        time.sleep(10)
        self.driver.quit()

def main():
    url = "http://google.co.jp"
    a = Sharch_data()
    a._Set_(url)
    a._fit_()
    a = None

if __name__=="__main__":
    main()


