
from gensim.models import word2vec
import logging
import sys


def main():
    logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s ", level = logging.INFO)

    sentences = word2vec.LineSentence(sys.argv[1])
    model = word2vec.Word2Vec(sentences, 
                            sg = 1,
                            size = 100,
                            min_count = 1,
                            window = 10,
                            hs = 1,
                            negative = 0)
    model.save(sys.argv[2])

if __name__=="__main__":
    main()

