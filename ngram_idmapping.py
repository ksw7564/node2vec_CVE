
import csv

import pandas as pd
import numpy as np

CVE_ID = []
IDF = []
with open('./5year/n_idf_integer_five_year.csv', 'r', encoding='UTF8') as f:
    reader = csv. reader(f)
    P = []
    for row in reader:
        P.append(row)#column

    for row in range(len(P)):
        line = []
        for j in range(1):
            line.append(str(P[row][0]))
        IDF.append(line)
print(IDF[0])
with open('./5year/cve-five-ngram.csv', 'r', encoding="UTF8") as f:
    reader = csv.reader(f)
    for line in reader:
        for txt in line:
            search = "cve-"
            o = 0
            if search in str(txt):
                cvtxt = txt
            else:
                for lst in IDF:
                    if txt in lst:
                        IDF[o].append(cvtxt)
                    o += 1


print(IDF[0])
csvfile = open("5year_inverted.csv", "w", newline="", encoding="UTF8")

csvwriter = csv.writer(csvfile)
for row in IDF:
    csvwriter.writerow(row)

csvfile.close()