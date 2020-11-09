import csv
import numpy
import math
import pandas as pd
#분산도 구하고 중앙값도 구하고, 클러스터별로 정렬도 한파일

with open("./20K_클러스터파일/20K_notcos.csv", 'r', encoding="utf8") as f:
    reader = csv.reader(f)
    twolist = []
    for row in reader:
        twolist.append(row)

plist = sorted(twolist, key=lambda row: row[1])
#그냥 정렬이 하고싶었음 클러스터별로 정렬됨(그럼 연산좀더 빠를꺼같아서)
list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []
list17 = []
list18 = []
list19 = []

#각클러스터별 분리
for i in range(len(plist)):
    if plist[i][1] == "0":
        list0.append(plist[i])
    elif plist[i][1] == "1":
        list1.append(plist[i])
    elif plist[i][1] == "2":
        list2.append(plist[i])
    elif plist[i][1] == "3":
        list3.append(plist[i])
    elif plist[i][1] == "4":
        list4.append(plist[i])
    elif plist[i][1] == "5":
        list5.append(plist[i])
    elif plist[i][1] == "6":
        list6.append(plist[i])
    elif plist[i][1] == "7":
        list7.append(plist[i])
    elif plist[i][1] == "8":
        list8.append(plist[i])
    elif plist[i][1] == "9":
        list9.append(plist[i])
    elif plist[i][1] == "10":
        list10.append(plist[i])
    elif plist[i][1] == "11":
        list11.append(plist[i])
    elif plist[i][1] == "12":
        list12.append(plist[i])
    elif plist[i][1] == "13":
        list13.append(plist[i])
    elif plist[i][1] == "14":
        list14.append(plist[i])
    elif plist[i][1] == "15":
        list15.append(plist[i])
    elif plist[i][1] == "16":
        list16.append(plist[i])
    elif plist[i][1] == "17":
        list17.append(plist[i])
    elif plist[i][1] == "18":
        list18.append(plist[i])
    elif plist[i][1] == "19":
        list19.append(plist[i])

nodeamount = []#각 클러스터별 갯수 확인 리스트
nodeamount.append(len(list0))
nodeamount.append(len(list1))
nodeamount.append(len(list2))
nodeamount.append(len(list3))
nodeamount.append(len(list4))
nodeamount.append(len(list5))
nodeamount.append(len(list6))
nodeamount.append(len(list7))
nodeamount.append(len(list8))
nodeamount.append(len(list9))
nodeamount.append(len(list10))
nodeamount.append(len(list11))
nodeamount.append(len(list12))
nodeamount.append(len(list13))
nodeamount.append(len(list14))
nodeamount.append(len(list15))
nodeamount.append(len(list16))
nodeamount.append(len(list17))
nodeamount.append(len(list18))
nodeamount.append(len(list19))
#각 클러스터별 중점을 찾기위한 리스트들
sum = [0]*100
sum1 = [0]*100
sum2 = [0]*100
sum3 = [0]*100
sum4 = [0]*100
sum5 = [0]*100
sum6 = [0]*100
sum7 = [0]*100
sum8 = [0]*100
sum9 = [0]*100
sum10 = [0]*100
sum11 = [0]*100
sum12 = [0]*100
sum13 = [0]*100
sum14 = [0]*100
sum15 = [0]*100
sum16 = [0]*100
sum17 = [0]*100
sum18 = [0]*100
sum19 = [0]*100

#클러스터별 중앙값계산과정
for i in range(len(list0)):
    for j in range(2, len(list0[i])):
        sum[j-2] = float(list0[i][j])
for i in range(len(list1)):
    for j in range(2, len(list1[i])):
        sum1[j-2] = float(list1[i][j])
for i in range(len(list2)):
    for j in range(2, len(list2[i])):
        sum2[j-2] = float(list2[i][j])
for i in range(len(list3)):
    for j in range(2, len(list3[i])):
        sum3[j-2] = float(list3[i][j])
for i in range(len(list4)):
    for j in range(2, len(list4[i])):
        sum4[j-2] = float(list4[i][j])
for i in range(len(list5)):
    for j in range(2, len(list5[i])):
        sum5[j-2] = float(list5[i][j])
for i in range(len(list6)):
    for j in range(2, len(list6[i])):
        sum6[j-2] = float(list6[i][j])
for i in range(len(list7)):
    for j in range(2, len(list7[i])):
        sum7[j-2] = float(list7[i][j])
for i in range(len(list8)):
    for j in range(2, len(list8[i])):
        sum8[j-2] = float(list8[i][j])
for i in range(len(list9)):
    for j in range(2, len(list9[i])):
        sum9[j-2] = float(list9[i][j])
for i in range(len(list10)):
    for j in range(2, len(list10[i])):
        sum10[j-2] = float(list10[i][j])
for i in range(len(list11)):
    for j in range(2, len(list11[i])):
        sum11[j-2] = float(list11[i][j])
for i in range(len(list12)):
    for j in range(2, len(list12[i])):
        sum12[j-2] = float(list12[i][j])
for i in range(len(list13)):
    for j in range(2, len(list13[i])):
        sum13[j-2] = float(list13[i][j])
for i in range(len(list14)):
    for j in range(2, len(list14[i])):
        sum14[j-2] = float(list14[i][j])
for i in range(len(list15)):
    for j in range(2, len(list15[i])):
        sum15[j-2] = float(list15[i][j])
for i in range(len(list16)):
    for j in range(2, len(list16[i])):
        sum16[j-2] = float(list16[i][j])
for i in range(len(list17)):
    for j in range(2, len(list17[i])):
        sum17[j-2] = float(list17[i][j])
for i in range(len(list18)):
    for j in range(2, len(list18[i])):
        sum18[j-2] = float(list18[i][j])
for i in range(len(list19)):
    for j in range(2, len(list19[i])):
        sum19[j-2] = float(list19[i][j])
#클러스터별 중앙값 계산
for i in range(len(sum)):
    sum[i] = sum[i]/nodeamount[0]

for i in range(len(sum1)):
    sum1[i] = sum1[i]/nodeamount[1]

for i in range(len(sum2)):
    sum2[i] = sum2[i]/nodeamount[2]
for i in range(len(sum3)):
    sum3[i] = sum3[i]/nodeamount[3]
for i in range(len(sum4)):
    sum4[i] = sum4[i]/nodeamount[4]
for i in range(len(sum5)):
    sum5[i] = sum5[i]/nodeamount[5]
for i in range(len(sum6)):
    sum6[i] = sum6[i]/nodeamount[6]
for i in range(len(sum7)):
    sum7[i] = sum7[i]/nodeamount[7]
for i in range(len(sum8)):
    sum8[i] = sum8[i]/nodeamount[8]
for i in range(len(sum9)):
    sum9[i] = sum9[i]/nodeamount[9]
for i in range(len(sum10)):
    sum10[i] = sum10[i]/nodeamount[10]
for i in range(len(sum11)):
    sum11[i] = sum11[i]/nodeamount[11]
for i in range(len(sum12)):
    sum12[i] = sum12[i]/nodeamount[12]
for i in range(len(sum13)):
    sum13[i] = sum13[i]/nodeamount[13]
for i in range(len(sum14)):
    sum14[i] = sum14[i]/nodeamount[14]
for i in range(len(sum15)):
    sum15[i] = sum15[i]/nodeamount[15]
for i in range(len(sum16)):
    sum16[i] = sum16[i]/nodeamount[16]
for i in range(len(sum17)):
    sum17[i] = sum17[i]/nodeamount[17]
for i in range(len(sum18)):
    sum18[i] = sum18[i]/nodeamount[18]
for i in range(len(sum19)):
    sum19[i] = sum19[i]/nodeamount[19]

def euclidean_distance(pt1, pt2):#각 노드별 중앙값기준의 거리 계산 함수
    puty = []
    for i in range(len(pt2)):
        distance = 0
        for j in range(2, len(pt2[i])):
            distance += (pt1[j-2] - float(pt2[i][j])) ** 2
        distance = distance ** 0.5
        puty.append(distance)
    return puty


distance_list = []#각 클러스터 중점으로부터의 노드 거리 리스트
distance_list.append(euclidean_distance(sum, list0))
distance_list.append(euclidean_distance(sum, list1))
distance_list.append(euclidean_distance(sum, list2))
distance_list.append(euclidean_distance(sum, list3))
distance_list.append(euclidean_distance(sum, list4))
distance_list.append(euclidean_distance(sum, list5))
distance_list.append(euclidean_distance(sum, list6))
distance_list.append(euclidean_distance(sum, list7))
distance_list.append(euclidean_distance(sum, list8))
distance_list.append(euclidean_distance(sum, list9))
distance_list.append(euclidean_distance(sum, list10))
distance_list.append(euclidean_distance(sum, list11))
distance_list.append(euclidean_distance(sum, list12))
distance_list.append(euclidean_distance(sum, list13))
distance_list.append(euclidean_distance(sum, list14))
distance_list.append(euclidean_distance(sum, list15))
distance_list.append(euclidean_distance(sum, list16))
distance_list.append(euclidean_distance(sum, list17))
distance_list.append(euclidean_distance(sum, list18))
distance_list.append(euclidean_distance(sum, list19))

id_dis0 = {}
id_dis1 = {}
id_dis2 = {}
id_dis3 = {}
id_dis4 = {}
id_dis5 = {}
id_dis6 = {}
id_dis7 = {}
id_dis8 = {}
id_dis9 = {}
id_dis10 = {}
id_dis11 = {}
id_dis12 = {}
id_dis13 = {}
id_dis14 = {}
id_dis15 = {}
id_dis16 = {}
id_dis17 = {}
id_dis18 = {}
id_dis19 = {}

#각 클러스터에대한 노드의 거리 가지고 있으므로 (노드 거리별로 제곱합)/노드의수 = 분산
for i in range(len(distance_list)):
    for j in range(len(distance_list[0])):
        id_dis0[list0[j][0]] = float(distance_list[0][j])
id_dis_li0 = sorted(id_dis0.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[1])):
        id_dis1[list1[j][0]] = float(distance_list[1][j])
id_dis_li1 = sorted(id_dis1.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[2])):
        id_dis2[list2[j][0]] = float(distance_list[2][j])
id_dis_li2 = sorted(id_dis2.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[3])):
        id_dis3[list3[j][0]] = float(distance_list[3][j])
id_dis_li3 = sorted(id_dis3.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[4])):
        id_dis4[list4[j][0]] = float(distance_list[4][j])
id_dis_li4 = sorted(id_dis4.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[5])):
        id_dis5[list5[j][0]] = float(distance_list[5][j])
id_dis_li5 = sorted(id_dis5.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[6])):
        id_dis6[list6[j][0]] = float(distance_list[6][j])
id_dis_li6 = sorted(id_dis6.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[7])):
        id_dis7[list7[j][0]] = float(distance_list[7][j])
id_dis_li7 = sorted(id_dis7.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[8])):
        id_dis8[list8[j][0]] = float(distance_list[8][j])
id_dis_li8 = sorted(id_dis8.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[9])):
        id_dis9[list9[j][0]] = float(distance_list[9][j])
id_dis_li9 = sorted(id_dis9.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[10])):
        id_dis10[list10[j][0]] = float(distance_list[10][j])
id_dis_li10 = sorted(id_dis10.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[11])):
        id_dis11[list11[j][0]] = float(distance_list[11][j])
id_dis_li11 = sorted(id_dis11.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[12])):
        id_dis12[list12[j][0]] = float(distance_list[12][j])
id_dis_li12 = sorted(id_dis12.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[13])):
        id_dis13[list13[j][0]] = float(distance_list[13][j])
id_dis_li13 = sorted(id_dis13.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[14])):
        id_dis14[list14[j][0]] = float(distance_list[14][j])
id_dis_li14 = sorted(id_dis14.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[15])):
        id_dis15[list15[j][0]] = float(distance_list[15][j])
id_dis_li15 = sorted(id_dis15.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[16])):
        id_dis16[list16[j][0]] = float(distance_list[16][j])
id_dis_li16 = sorted(id_dis16.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[17])):
        id_dis17[list17[j][0]] = float(distance_list[17][j])
id_dis_li17 = sorted(id_dis17.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[18])):
        id_dis18[list18[j][0]] = float(distance_list[18][j])
id_dis_li18 = sorted(id_dis18.items(), key=lambda t : t[1])

for i in range(len(distance_list)):
    for j in range(len(distance_list[19])):
        id_dis19[list19[j][0]] = float(distance_list[19][j])
id_dis_li19 = sorted(id_dis19.items(), key=lambda t : t[1])
total = []#다 합침.
total.append(id_dis_li0)
total.append(id_dis_li1)
total.append(id_dis_li2)
total.append(id_dis_li3)
total.append(id_dis_li4)
total.append(id_dis_li5)
total.append(id_dis_li6)
total.append(id_dis_li7)
total.append(id_dis_li8)
total.append(id_dis_li9)
total.append(id_dis_li10)
total.append(id_dis_li11)
total.append(id_dis_li12)
total.append(id_dis_li13)
total.append(id_dis_li14)
total.append(id_dis_li15)
total.append(id_dis_li16)
total.append(id_dis_li17)
total.append(id_dis_li18)
total.append(id_dis_li19)
for i in range(len(total)):#각 노드의 클러스터위치를 연산하기위해 썻는데 auto파일에 자동화시켰음.
    for j in range(len(total[i])):
        if 'cve-2017-18403' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2019-4439' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2015-4812' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2018-7034' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2017-6553' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2017-10915' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2015-5791' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2019-3833' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2017-18383' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2019-10997' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2016-9393' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2018-7738' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2017-16197' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2017-11536' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2017-6381' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2019-2756' in total[i][j]:
            print(i)
for i in range(len(total)):
    for j in range(len(total[i])):
        if 'cve-2015-0536' in total[i][j]:
            print(i)




#클러스터넘버 추가
for i in range(len(total)):
    total[i].insert(0, i)

for i in  range(len(nodeamount)):
    total[i].insert(1, int(nodeamount[i]))

SSum = []
SSum.append(sum)
SSum.append(sum1)
SSum.append(sum2)
SSum.append(sum3)
SSum.append(sum4)
SSum.append(sum5)
SSum.append(sum6)
SSum.append(sum7)
SSum.append(sum8)
SSum.append(sum9)
SSum.append(sum10)
SSum.append(sum11)
SSum.append(sum12)
SSum.append(sum13)
SSum.append(sum14)
SSum.append(sum15)
SSum.append(sum16)
SSum.append(sum17)
SSum.append(sum18)
SSum.append(sum19)

bbunsan = []#클러스터별 분산계산 리스트
bsum = 0
for i in range(len(distance_list[0])):
    bsum += (distance_list[0][i])**2
bunsan = bsum/len(distance_list[0])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[1])):
    bsum += (distance_list[1][i])**2
bunsan = bsum/len(distance_list[1])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[2])):
    bsum += (distance_list[2][i])**2
bunsan = bsum/len(distance_list[2])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[3])):
    bsum += (distance_list[3][i])**2
bunsan = bsum/len(distance_list[3])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[4])):
    bsum += (distance_list[4][i])**2
bunsan = bsum/len(distance_list[4])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[5])):
    bsum += (distance_list[5][i])**2
bunsan = bsum/len(distance_list[5])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[6])):
    bsum += (distance_list[6][i])**2
bunsan = bsum/len(distance_list[6])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[7])):
    bsum += (distance_list[7][i])**2
bunsan = bsum/len(distance_list[7])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[8])):
    bsum += (distance_list[8][i])**2
bunsan = bsum/len(distance_list[8])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[9])):
    bsum += (distance_list[9][i])**2
bunsan = bsum/len(distance_list[9])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[10])):
    bsum += (distance_list[10][i])**2
bunsan = bsum/len(distance_list[10])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[11])):
    bsum += (distance_list[11][i])**2
bunsan = bsum/len(distance_list[11])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[12])):
    bsum += (distance_list[12][i])**2
bunsan = bsum/len(distance_list[12])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[13])):
    bsum += (distance_list[13][i])**2
bunsan = bsum/len(distance_list[13])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[14])):
    bsum += (distance_list[14][i])**2
bunsan = bsum/len(distance_list[14])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[15])):
    bsum += (distance_list[15][i])**2
bunsan = bsum/len(distance_list[15])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[16])):
    bsum += (distance_list[16][i])**2
bunsan = bsum/len(distance_list[17])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[17])):
    bsum += (distance_list[17][i])**2
bunsan = bsum/len(distance_list[17])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[18])):
    bsum += (distance_list[18][i])**2
bunsan = bsum/len(distance_list[18])
bbunsan.append(bunsan)

bsum = 0
for i in range(len(distance_list[19])):
    bsum += (distance_list[19][i])**2
bunsan = bsum/len(distance_list[19])
bbunsan.append(bunsan)
#분산을구할꺼임 (평균값-현재값=구해놈)^2을 다더하고 /
# print(bbunsan)

davg = pd.DataFrame(SSum)
dp = pd.DataFrame(bbunsan)

#df.to_csv('20K_notcos_notword_sort.csv')

