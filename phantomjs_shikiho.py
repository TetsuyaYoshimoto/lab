
#encoding=shitf-jis

from selenium import webdriver
import csv


def get_data(number):
    driver = webdriver.PhantomJS(your write full path at phantomjs)
    url = "http://shikiho.jp/tk/stock/info/" + str(number)
    driver.get(url)
    html = driver.page_source
    driver.quit()
    driver = None
    
    html = html.encode("utf-8")


    f = open("./shikiho_data/" + str(number) + ".txt", "w")
    f.write(html)
    f.close()

def main():
    f = open("./output2.csv", "r")
    reader = csv.reader(f)
    count = 1
    for row in reader:
        if count > YOUR_SET_NUMBER:
            try:
                get_data(row[0])
                print row[0], " | ", str(count) + "/1108", (float(count)/1108.)*100, "%"
            except:
                try:
                    get_data(row[0])
                    print row[0], " | ", str(count) + "/1108", (float(count)/1108.)*100, "%"
                except:
                    try:
                        get_data(row[0])
                        print row[0], " | ", str(count) + "/1108", (float(count)/1108.)*100, "%"
                    except:
                        print row[0], " | ", str(count) + "/1108", (float(count)/1108.)*100, "%", "NG"
        count += 1

if __name__=="__main__":
    main()


