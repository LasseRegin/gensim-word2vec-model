
import os

import gensim

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
MODEL_PATH  = os.path.join(SCRIPT_PATH, 'model/')

if __name__ == '__main__':

    # Load word2vec model
    model = gensim.models.Word2Vec.load(os.path.join(MODEL_PATH, 'word2vec.model'), mmap='r')

    print('King - man + woman:')
    for word, sim in model.most_similar(positive=['woman', 'king'], negative=['man']):
        print('\"%s\" - similarity: %g' % (word, sim))
    print('')

    print('Similarity between man and woman:')
    print(model.similarity('woman', 'man'))
