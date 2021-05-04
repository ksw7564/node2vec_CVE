import warnings

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

G = nx.Graph()

# List 속성
CVE_ID = []
CWE_ID = []
Vulnerability_Types = []
Score = []
Text = []
Gained_Access_Level = []
Access = []
Complexity = []
Authentication = []
Conf = []
Integ = []
Avail = []
ptilt = []
Text2 = []
Text3 = []

G.add_nodes_from(CVE_ID, kind='CVE_ID')
# G.add_nodes_from(CWE_ID, kind='CWE_ID')
# G.add_nodes_from(Vulnerability_Types, kind='Vulnerability_Types')
# G.add_nodes_from(Score, kind='Score')
G.add_nodes_from(Text, kind='Text')
G.add_nodes_from(Text2, kind='Text2')
G.add_nodes_from(Text3, kind='Text3')
# G.add_nodes_from(Gained_Access_Level, kind='Gained_Access_Level')
# G.add_nodes_from(Access, kind='Access')
# G.add_nodes_from(Complexity, kind='Complexity')
# G.add_nodes_from(Authentication, kind='Authentication')
# G.add_nodes_from(Conf, kind='Conf')
# G.add_nodes_from(Integ, kind='Integ')
# G.add_nodes_from(Avail, kind='Avail')


with open('cve-test-tri.csv', 'r', encoding="UTF8") as f:
    reader = csv.reader(f)
    rupe = 0
    u = 0
    # for u in range(0, 100):
    #   u += 1
    for line in reader:
        for txt in line:
            myHost = "CVE-"
            if myHost in txt:
                CVE_ID.append(str(txt))

            # elif txt == null:
            #     print
            #     continue
            else:
                Text3.append(str(txt))

with open('cve-test-token-stem.csv', 'r', encoding="UTF8") as f:
    reader = csv.reader(f)
    for line in reader:
        for txt in line:
            myHost = "CVE-"
            if myHost in txt:
                continue

            # elif txt == null:
            #     print
            #     continue
            else:
                Text.append(str(txt))

with open('cve-test-bi.csv', 'r', encoding="UTF8") as f:
    reader = csv.reader(f)
    for line in reader:
        for txt in line:
            myHost = "CVE-"
            if myHost in txt:
                continue

            # elif txt == null:
            #     print
            #     continue
            else:
                Text2.append(str(txt))

G.add_nodes_from(CVE_ID, kind='CVE_ID')
# G.add_nodes_from(CWE_ID, kind='CWE_ID')
# G.add_nodes_from(Score, kind='Score')
# G.add_nodes_from(Gained_Access_Level, kind='Gained_Access_Level')
G.add_nodes_from(Text, kind='Text')
G.add_nodes_from(Text2, kind='Text2')
G.add_nodes_from(Text3, kind='Text3')
# G.add_nodes_from(Access, kind='Access')
# G.add_nodes_from(Complexity, kind='Complexity')
# G.add_nodes_from(Authentication, kind='Authentication')
# G.add_nodes_from(Conf, kind='Conf')
# G.add_nodes_from(Integ, kind='Integ')
# G.add_nodes_from(Avail, kind='Avail')
# G.add_nodes_from(CVE_ID, kind='list')


with open('cve-test-tri.csv', 'r', encoding="UTF8") as f:
    reader = csv.reader(f)
    # for u in range(0, 10):
    # u += 1
    for line in reader:
        for txt in line:
            myHost = "CVE-"  # http:// http
            if myHost in txt:
                start_edge = str(txt)

            else:
                end_edge = str(txt)
                G.add_edge(start_edge, end_edge)

with open('cve-test-token-stem.csv', 'r', encoding="UTF8") as f:
    reader = csv.reader(f)
    u = 0
    # for u in range(0, 10):
    # u += 1
    for line in reader:
        for txt in line:
            myHost = "CVE-"
            if myHost in txt:
                start_edge = str(txt)

            else:
                end_edge = str(txt)
                G.add_edge(start_edge, end_edge)

with open('cve-test-bi.csv', 'r', encoding="UTF8") as f:
    reader = csv.reader(f)
    u = 0
    # for u in range(0, 10):
    # u += 1
    for line in reader:
        for txt in line:
            myHost = "CVE-"
            if myHost in txt:
                start_edge = str(txt)

            else:
                end_edge = str(txt)
                G.add_edge(start_edge, end_edge)

# nx.draw(G, with_labels=True)
# plt.show()

node2vec = Node2Vec(graph=G,  # target graph
                    dimensions=50,  # embedding dimension
                    walk_length=30,  # number of nodes in each walks
                    p=1,  # return hyper parameterp가 높아지면, 이전에 방문했던 노드로는 잘 가지 않고, 새로운 노드로 가는 경향성이 높아지며,
                    q=0.0001,
                    # inout parameter, q값을 작게 하면 structural equivalence를 강조하는 형태로 학습됩니다. q가 낮아지면, 새로운 노드로 가는 경향성이 높아지죠
                    num_walks=200,
                    workers=4,
                    )

model1 = node2vec.fit(window=10)

# kmeans = KMeans(n_clusters=5, random_state=0).fit(model1.wv.vectors)

edges_embs = HadamardEmbedder(keyed_vectors=model1.wv)

#print(edges_embs[('CVE-2019-1020018', 'before 1.0.0a12 allow')])
print(G.nodes)
print(G.edges)
edges_kv = edges_embs.as_keyed_vectors()

print(model1.most_similar(positive=str("CVE-2019-1020018")))

# print(edges_kv.most_similar(str(('1', '2')), topn=20))
print(edges_kv.most_similar(str(('CVE-2019-1020019', 'host')), topn=20))

for node, _ in model1.most_similar('CVE-2019-1020019'):
    print(node, _)


print(edges_embs)

model1.most_similar('CVE-2019-1020018')
print("202줄")
model1.most_similar(str("buffer overflow"))
print("204줄")
print(model1.most_similar(str("buffer overflow")))
print("206줄")
print(model1.most_similar(str("CVE-2019-1020018")))

print(" tt")

print(model1.most_similar(positive=str("CVE-2019-1010292")))

print(" tt")

print(edges_kv.most_similar(positive=[str(('CVE-2019-1010292', 'buffer overflow'))], negative=[str(('CVE-2019-1020018', 'frame'))], topn=20))
print("쉼")
print(edges_kv.most_similar(positive=[str(('CVE-2019-1010292', 'buffer overflow'))], negative=[str(('CVE-2019-1020018', 'frame'))]))
