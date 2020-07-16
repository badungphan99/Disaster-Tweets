import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import torch

from gensim.models.keyedvectors import KeyedVectors

import nltk
nltk.download('punkt')
nltk.download('stopwords')

from cleaningtext import *
from visualize import *

def normData(path: str):
    data = pd.read_csv(path)

    #clean emoji, url, ...
    data = clean(data)

    #tokenizing text
    data['token'] = data['clean_text'].apply(nltk.tokenize.word_tokenize)

    data['lower'] = data['token'].apply(lambda x: [word.lower() for word in x])

    #remove stop word
    stop = set(nltk.corpus.stopwords.words('english'))
    data['stopword_remove'] = data['lower'].apply(lambda x: [word for word in x if word not in stop])

    return data

def train():
    traindata = normData('/mnt/32D84D55D84D188D/NLP-data/nlp-getting-started/train.csv')
    testdata = normData('/mnt/32D84D55D84D188D/NLP-data/nlp-getting-started/test.csv')

    # optimizer = torch.optim.Adam(model.parameters(), lr= 0.0001)

    word_vectors = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)
    wv_matrix = []



if __name__ == "__main__":
    #normalize data
    data = normData('/mnt/32D84D55D84D188D/NLP-data/nlp-getting-started/train.csv')
    train()
    # vis.targetDistribution(data)