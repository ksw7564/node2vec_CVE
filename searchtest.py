import warnings

from pyasn1.compat.octets import null
from text_unidecode import unidecode
from collections import deque
#단순 유사도 구하기위해 던진파일
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
from gensim.models import Word2Vec, KeyedVectors
from gensim.test.utils import common_texts, get_tmpfile

model2 = Word2Vec.load('./nodemodel/node2vec_notcos.model')
# print(model2.most_similar(positive=[str('cve-2019-16222')], topn=20))
# print("하나")
# print(model2.most_similar(positive=["cve-2019-16222"], negative=[str("wordpress")], topn=20))
# print("둘")
# print(model2.most_similar(positive=[str('cve-2019-16222')], negative=[str('wordpress'), str('javascript')], topn=20))
# print("0클러스터와 4클러스터의 중심노드")
# print(model2.most_similar(positive=[str('cve-2018-15858'), str('cve-2015-9455')], topn=20))
# print("0클러스터와 4클러스터의 중점으로부터 천번째 노드")
# print(model2.most_similar(positive=[str('cve-2018-15858'), str('cve-2018-14707')], topn=20))
# print("9클러스터 2개 - 11클러스터(정보를얻다+정보를얻다-서비스거부)")
# print(model2.most_similar(positive=[str('cve-2019-1125'), str('cve-2015-3058')], negative=[str('cve-2018-18892')], topn=20))
# print("19클러스터2개 - 14클러스터(정보를얻다+정보를얻다-버퍼 오버플로우로인한 서비스거부)")
# print(model2.most_similar(positive=[str('cve-2017-8523'), str('cve-2015-4108')], negative=[str('cve-2017-9904')], topn=20))
# #0클
# print(model2.most_similar(positive=["cve-2018-3046", "cve-2018-11087"], topn=20))
# #1클러
# print(model2.most_similar(positive=["cve-2016-8403", "cve-2016-8405"], topn=20))
# #2클러
# print(model2.most_similar(positive=["cve-2015-9455", "cve-2018-6031"], topn=20))
listt = list(model2.most_similar(positive=[str('cve-2018-15858'), str('cve-2015-9455')], topn=20))

print(listt[0][0])
print(listt[0][1])