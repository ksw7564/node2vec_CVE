import itertools
import warnings

import matplotlib
from pyasn1.compat.octets import null
from sklearn.metrics import silhouette_score
from text_unidecode import unidecode
from collections import deque

warnings.filterwarnings('ignore')
import csv

import pandas as pd
from sklearn.manifold import TSNE
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import  matplotlib.font_manager as fm
import matplotlib.patches as mpatcheso
import seaborn as sns
from node2vec import Node2Vec
from node2vec.edges import HadamardEmbedder
import re
from sklearn.decomposition import PCA
from stellargraph import datasets
from sklearn.preprocessing import MinMaxScaler
from IPython.display import display, HTML
from sklearn.cluster import KMeans
from sklearn import cluster
from sklearn import metrics
from gensim.models import Word2Vec
from gensim.test.utils import common_texts, get_tmpfile

model2 = Word2Vec.load('./nodemodel/node2vec2.model')

ks = range(1, 11)  # for 1 to 10 clusters
word_vectors = model2.wv.syn0
# sse = []
sil = []
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

X, y = make_blobs(n_samples=500, n_features=2,
                  centers=4,
                  cluster_std=1,
                  center_box=(-10.0, 10.0),
                  shuffle=True,
                  random_state=1)
# start the cluster range from 2
range_n_clusters = range(5, 50, 5)
for n_clusters in range_n_clusters:
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(word_vectors)
    silhouette_avg = silhouette_score(word_vectors, cluster_labels)
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)
    sil.append(silhouette_avg)

print(sil)