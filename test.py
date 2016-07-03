
import os
import sys
import logging

import gensim

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
MODEL_PATH  = os.path.join(SCRIPT_PATH, 'model/')

if __name__ == '__main__':

    # Initialize logging
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    logging.info('Loading word2vec model..')
    model = gensim.models.Word2Vec.load(os.path.join(MODEL_PATH, 'word2vec.model'), mmap='r')

    print(model.most_similar(positive=['woman', 'king'], negative=['man']))
    print(model.similarity('woman', 'man'))
