
#encoding=utf-8

from gensim.models import word2vec
import sys

def main():
    for _ in range(4):
        word = input()
        print(word)
        model = word2vec.Word2Vec.load("../out.model")
        results = model.most_similar(positive=word, topn=int(10))
        
        for result in results:
            print(result[0], "\t", result[1])
        print("==================================")

if __name__=="__main__":
    main()

