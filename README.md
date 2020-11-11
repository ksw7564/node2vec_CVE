# node2vec_CVE

node2vec Backup material

data_file is CVE -> Pretreatment

This project was launched to create a data vulnerability category using cve.
Using word2vec's language model was expected not to generate cve details and other information.
So I decided to approach the graph model. I decided to use cve_id and freetext for the graph.
Since Freetext contains analytics such as details about vulnerabilities and the areas they belong to, we decided to create a new perspective with Freetext.
The goal is to use cve_id for 5 years.
The latest security vulnerability information is the most accurate to post to the community, and free text is provided to help you clarify the words that matter most. (Scalability)
Of course I think the important words can be removed via idf, but I excluded them.
The main program, such as the operating system or windows, may be considered important, but it is because the categories are too large.

As a result the nodes will be cve_id and idf (free text).
If cve_id refers to idf, create an edge connecting the nodes.
However, cve_ids are not linked to each other. This means you have to go through idf to find a connection with another cve_id. The expected graph inclusion is as follows:

CVE_ID ——— IDF (Free Text) ——— CVE_ID

The algorithm that generates a model using this graph uses Node2vec.
The reason for the choice is that Node2vec decided to use randomwalk, which is a way to reach distant nodes unlike Word2vec.

Node2vec is basically Word2vec based, so the dimension and window concept are the same. walk_length: 30 The number of feet in each node (need to adjust) P = 1, Q = 0.0001 P is greatly reduced to Q so that it can be included in the far node. Workers: 4 Number of workers running in parallel Window: 5 (I saw that large scale data is being generated.

You can use this model to achieve similarity, but you cannot evaluate the entire data. Clustering was used for this. I used the simplest KMeans clustering.

For this, I decided on K with the elbow and silhouette, but did not get a good score. So, I used about 20 (operating systems, programs, information access, vulnerability categories) K as the categories I thought of.

I think the results are okay. Searching for the similarity of CVE_ID + CVE_ID is usually identified as pointing to one cluster. I think you can get better results if you use a cluster other than Kmeans for finer clustering.

Cluster Analysis Results: Cluster 0 (first cluster) was mostly a vulnerability in data collection. There are a few pointless clusters and no other cluster features. (Lack of knowledge about security data seems to be the cause.)

An example of similarity is teaching about 60% of cve_id nodes in cluster 8 when using the two nodes closest to the center of cluster 0.

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
