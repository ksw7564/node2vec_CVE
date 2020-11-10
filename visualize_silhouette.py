import itertools
import warnings

import matplotlib
from pyasn1.compat.octets import null
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
from sklearn import metrics
from gensim.models import Word2Vec
from gensim.test.utils import common_texts, get_tmpfile


scaler = MinMaxScaler(feature_range=(0, 1))

model2 = Word2Vec.load('./nodemodel/node2vec2.model')

#
word_vectors = model2.wv.syn0
#num_clusters = word_vectors.shape[0] / 5
#print(num_clusters)
#num_clusters = int(num_clusters)

kmeans_clustering = KMeans(n_clusters=20).fit(word_vectors)
labels = kmeans_clustering.labels
idx = kmeans_clustering.fit_predict(word_vectors)
idf = kmeans_clustering.cluster_centers_#중앙
idx = list(idx)
names = model2.wv.index2word
silhouette_score = metrics.silhouette_score(word_vectors, idx, metric='euclidean')
word_centroid_map = {names[i]: idx[i] for i in range(len(names))}
print(kmeans_clustering)
print(idx)
print(labels)
# num_clusters

matplotlib.rcParams["axes.unicode_minus"] = False

print("silhouette_score:")
print(silhouette_score)
