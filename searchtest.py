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
import time
from gensim.models import Word2Vec
from gensim.test.utils import common_texts, get_tmpfile

model2 = Word2Vec.load('node2vec2.model')
print(model2.most_similar(positive=[str('CVE-2019-16222')], topn=20))
print("하나")
print(model2.most_similar(positive=["CVE-2019-16222"], negative=[str("wordpress")], topn=20))
print("둘")
print(model2.most_similar(positive=[str('CVE-2019-16222')], negative=[str('wordpress'), str('javascript')], topn=20))
