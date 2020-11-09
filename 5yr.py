import warnings
#모델 생성 파일입니다.
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
import matplotlib.patches as mpatcheso
import seaborn as sns
from node2vec import Node2Vec
from node2vec.edges import HadamardEmbedder
import re
from sklearn.decomposition import PCA
from stellargraph import datasets
from IPython.display import display, HTML
from sklearn.cluster import KMeans
import time
from gensim.models import Word2Vec
from gensim.test.utils import common_texts, get_tmpfile

G = nx.Graph()
all = []


#노드와 엣지파일 불러옴
with open('./5year/five_cos.csv', 'r', encoding="UTF8") as f2:
    reader = csv.reader(f2)

    P = []
    for line in reader:
        list = []
        for txt in line:
            list.append(txt)
        P.append(list)

#inverted 파일불러옴
with open('./5year/5year_inverted.csv', 'r', encoding="UTF8") as f:
    reader = csv.reader(f)

    X = []
    for line in reader:
        list = []
        for txt in line:
            list.append(txt)
        X.append(list)


CVE_ID = []
CVE_int = []
IDF = []
IDF_int = []
COCVE = []
Inv = []

rupb = True
for i in range(len(P)):#CVE 리스트
    t = P[i][0]
    if t == '':
        break
    CVE_ID.append(P[i][0])
    CVE_int.append(int(P[i][1]))
CVE_ID.sort()
CVE_int.sort()

for i in range(len(P)):#IDF 리스트
    for j in range(len(P[i])):
        t = P[i][j]
        if t == '':
            rupb = False
            break
    if rupb == False:
        break
    IDF.append(P[i][2])
    IDF_int.append(int(P[i][3]))
print(IDF)
# p = []
# e = []
# for i in range(len(P)):#cos 리스트
#     p.append(P[i][4])
#     e.append(P[i][5])
#
# COCVE.append(p)
# COCVE.append(e)
# del p, e

#노드생성
G.add_nodes_from(CVE_ID, kind='CVE_ID')
G.add_nodes_from(IDF, kind='IDF')

CVE_ID_all = []
CVE_ID_all.append(CVE_int)
CVE_ID_all.append(CVE_ID)

IDF_all = []
IDF_all.append(IDF_int)
IDF_all.append(IDF)
i = 0

for line in X:#inverted 인덱싱 리스트
    list = []
    j = 0
    for txt in line:
        if "cve-" in X[i][j]:
            list.append(X[i][j])
        j += 1
    Inv.append(list)
    i += 1

CVE_int, CVE_ID, IDF, IDF_int, P, list, X

#이거쓰면 cos 문서간 유사도 엣지생성인데 이거 없는게 처음 설계랑 잘맞고 결과도 좋음 그래도일단 남
for i in range(len(COCVE)): #cos 문서유사도간 엣지생성
    A = COCVE[0][i]
    B = COCVE[1][i]
    start_edge = A
    end_edge = B
    G.add_edge(start_edge, end_edge)

print(len(IDF_all[0]))
for i in range(len(IDF)): # CVE, IDF엣지 생성
    start_edge = IDF[i]
    B = Inv[i]
    for j in B:
        end_edge = j
        G.add_edge(start_edge, end_edge)

# nx.draw(G, with_labels=True)
# plt.show()
print(len(G.nodes()))
print(len(G.edges()))

#node2vec 모델 생성
# node2vec = Node2Vec(graph=G,  # target graph
#                     dimensions=100,  # embedding dimension
#                     walk_length=30,  # number of nodes in each walks
#                     p=1,
#                     # return hyper parameterp가 높아지면, 이전에 방문했던 노드로는 잘 가지 않고,
#                     # 새로운 노드로 가는 경향성이 높아지며,
#                     q=0.0001,
#                     # inout parameter, q값을 작게 하면 structural equivalence를 강조하는 형태로 학습됩니다.
#                     # q가 낮아지면, 새로운 노드로 가는 경향성이 높아지죠
#                     num_walks=200,
#                     workers=4,
#                     #temp_folder="tfold"
#                     )
#
# model1 = node2vec.fit(window=5)
# #함수 이름들 잘확인하면 됩니다.
# model1.wv.save_word2vec_format('node2vec_notword.txt', binary=False)
# #
# model2 = Word2Vec.load('node2vec_notword.model.model')
#

#edges_embs = HadamardEmbedder(keyed_vectors=model2.wv)

#print(edges_embs[('CVE-2019-1020018', 'before 1.0.0a12 allow')])
#print(G.nodes)
#print(G.edges)
#edges_kv = edges_embs.as_keyed_vectors()

# print(model2.most_similar(positive=str(namemapping("cve-2019-1010297"))))

# print(edges_kv.most_similar(str(('1', '2')), topn=20))
#print(edges_kv.most_similar(str(('CVE-2019-1020019', 'host')), topn=20))

# for node, _ in model2.most_similar('CVE-2019-1020019'):
#     print(node, _)



# model2.most_similar('CVE-2019-1020018')
# print("202줄")
# model2.most_similar(str("buffer overflow"))
# print("204줄")
# print(model2.most_similar(str("buffer overflow")))
# print("206줄")
# print(model2.most_similar(str("CVE-2019-1020018")))

# print(" tt")
# print(model2.most_similar(positive=[str('CVE-2019-16222')], negative=[str('wordpress')], topn=100))
# print(prinmapping(model2.most_similar(positive=[str(namemapping('cve-2019-5771'))], negative=[str(namemapping('wordpress'))], topn=100)))
#
# print(" tt")
# print(prinmapping(model2.most_similar(positive=[str(namemapping('CVE-2019-16222'))], negative=[str(namemapping('wordpress', 'javascript'))], topn=20)))
# #print(prinmapping(edges_kv.most_similar(positive=[str(namemapping('CVE-2019-16222'))], negative=[str(namemapping('wordpress', 'javascript'))], topn=20)))
# print("쉼")
# print(prinmapping(model2.most_similar(positive=[str(namemapping('CVE-2019-16222'))], negative=[str(namemapping('wordpress'))], topn=20)))
# #print(prinmapping(edges_kv.most_similar(positive=[str(namemapping('CVE-2019-16222'))], negative=[str(namemapping('wordpress'))], topn=100)))