import itertools
import warnings

import matplotlib
from pyasn1.compat.octets import null
from text_unidecode import unidecode
from collections import deque

warnings.filterwarnings('ignore')
import csv
from sklearn.datasets import make_blobs
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
from IPython.display import display, HTML
from sklearn.cluster import KMeans
from gensim.models import Word2Vec
from gensim.test.utils import common_texts, get_tmpfile
from itertools import chain

model2 = Word2Vec.load('./nodemodel/node2vec2.model')

#
word_vectors = model2.wv.syn0
#num_clusters = word_vectors.shape[0] / 5
#print(num_clusters)
#num_clusters = int(num_clusters)

kmeans_clustering = KMeans(n_clusters=20)
cut = kmeans_clustering.fit(word_vectors)
label = kmeans_clustering.labels_
kmeans_clustering.fit_transform()
idx = kmeans_clustering.fit_predict(word_vectors)
Xt = kmeans_clustering.fit_transform(word_vectors)
print(label)
# print(kmeans_clustering.cluster_centers_)
Xt = list(Xt)
idf = kmeans_clustering.cluster_centers_
idf = list(idf)
idx = list(idx)
names = model2.wv.index2word
center = []
# center = {idf[i]: names[i] for i in range(len(names))}
word_centroid_map = {names[i]: idx[i] for i in range(len(names))}
# num_clusters
#clust_list = []
#print(idf)
# for c in range(20):
#     # 클러스터 번호를 출력
#     print("\ncluster {}".format(c))
#     words = []
#     cluster_values = list(word_centroid_map.values())
#     for i in range(len(cluster_values)):
#         if (cluster_values[i] == c):
#             words.append(list(word_centroid_map.keys())[i])
#     clust_list.append()
#     print(words)

# print(word_centroid_map)
# print(word_centroid_map.keys())
# print(word_centroid_map.values())

matplotlib.rcParams["axes.unicode_minus"] = False

vocab = list(model2.wv.vocab)
X = model2[vocab]
# tsne = TSNE(n_components=2)
# X_tsne = tsne.fit_transform(X)
# df = pd.DataFrame(X_tsne, , index=vocab)

temp = []
for i in range(len(vocab)):
    a = names.index(vocab[i])
    temp.append(idx[a])

demen = []
print(len(Xt[0]))
for i in range(len(Xt)):
    to = []
    for j in range(len(Xt[i])):
       to.append(str(Xt[i][j]))
    demen.append(to)
#
# print(word_centroid_map.values())
# print(kmeans_clustering.cluster_centers_)
#
# print(word_centroid_map.key())

#
# f = open("20K_cos_word.csv", "w", encoding="UTF8")
#
# for i in range(len(vocab)):
#     f.write(vocab[i] + ',' + str(temp[i]))
#     for j in range(len(demen[i])):
#         f.write(',' + str(demen[i][j]))
#     f.write("\n")
#
# f.close()
