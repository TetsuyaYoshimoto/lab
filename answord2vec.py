
#encoding=utf-8

from gensim.models import word2vec
import sys

def main():
    word = input(Please Wrod : ")
    #Your put on model Path
    model = word2vec.Word2Vec.load("../out.model")
    #Output similer word top 10
    results = model.most_similar(positive=word, topn=int(10))
        
    for result in results:
        print(result[0], "\t", result[1])

if __name__=="__main__":
    main()
