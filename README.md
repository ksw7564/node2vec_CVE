# node2vec_CVE

node2vec Backup material

data_file is CVE -> Pretreatment

The project was launched to create categories of data vulnerabilities using cve.
It was expected that using the language model of word2vec would not produce information that is different from cve details.
So I decided to approach it as a graph model.
I decided to use cve_id and freetext for the graph.
Freetext includes detailed information on vulnerabilities and classification information such as areas to which they belong, so it is decided to produce a new perspective through freetext.
The goal is to use a five-year cve_id.
The latest security vulnerability information is most accurate to be posted on the community, and freetext is idfed for clarity to pick out the most important words. 
Of course, I think that important words can be removed through idf, but I excluded them.
This is because the operating system or major programs, such as the window, can be seen as important, but they are too large a category.

As a result, the node becomes cve_id and idf(freetext).
If cve_id refers to idf, create an edge to connect the nodes.
But cve_id is not connected to each other.
That is, to find connections with other cve_id, you must go through idf.
The expected graph inclusion is as follows:

CVE_ID ——— IDF(freetext) ——— CVE_ID

The algorithm to produce the model using this graph uses Node2vec.
The reason for selection is that Node2vec, unlike Word2vec, decided to use randomwalk, which is a way to reach distant nodes.

Because Node2vec is basically Word2vec based, the dimension and window concepts are the same.
walk_length : 30 Number of feet for each node (adjustment is required)
P = 1, Q = 0.0001
P is greatly reduced to Q so that it can be embedded to faraway nodes.
Workers : 4 Number of workers for parallel execution
Window : 5 (We have confirmed that larger and less relevant data is generated.)

# ngram_idmaping.Py
This is a file that maps to pre-processed data. 
It's exactly a reverse index job.
Because cve data file is large, it is to proceed using reverse index.

# 5yr.py
Use this file to create a node2vec model.
This file uses a machined dataset file (five_cos.csv, 5 year_inverted.csv).
The node2vec generation variable was determined by a number of experiments that I think are most accurate.
And tried to interact with distant nodes by taking advantage of the graph's characteristics.

# elbow.py and visualize_silhouette.py
These files were used to find K in proper clustering of models.
The result was hopeless.
There was no good evaluation of K and it was constant.
So I decided because I thought there were about 20 types of security vulnerabilities.

# sklearnkmeans.py
A clustering file.
We proceeded with 20K.
The clustering output and file generation are annotated.
This is used to print clustered results.
File creation is also annotated now.
