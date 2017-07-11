
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def main():
    rsrcmgr = PDFResourceManager()
    rettxt = StringIO()
    laparams = LAParams()

#    laparams.detect_vertical = True
    device = TextConverter(rsrcmgr, rettxt, codec = "utf-8", laparams = laparams)

    fp = open("test.pdf", "rb")
    interperter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.get_pages(fp,pagenos=None,maxpages=0,password=None,caching=True,check_extractable=True):
        interperter.process_page(page)

    print(rettxt.getvalue())

    fp.close()
    device.close()
    rettxt.close()


if __name__=="__main__":
    main()



