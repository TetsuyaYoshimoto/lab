
#encoding=utf-8

from gensim.models import word2vec
import sys

def main():
    model = word2vec.Word2Vec.load("out.model")
    while(True):
        try:
            posi = input("Please Positive word : ").split()
            if len(posi) != 0:
                break 
            print("Please Retry! ")
        except UnicodeDecodeError:
            print("Please Retry! ")

    while(True):
        try:
            nega = input("Please Negative word : ").split()
            break
        except UnicodeDecodeError:
            print("Please Retry! ")
    while(True):
        try:
            num = int(input("Please Top Number : "))
            break
        except ValueError:
            print("Please Retry! ")


    if len(posi) == 0: posi = ""
    if len(nega) == 0: nega = ""
    results = model.most_similar(positive=posi, negative=nega, topn=num)

    for result in results:
        print(result[0], "\t", result[1])

if __name__=="__main__":
    main()


