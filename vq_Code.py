#!/usr/bin/python
# coding:utf-8

from random import randint


# 欧几里得距离计算,返回平方差之和
def sim_distance(v1, v2):
    sums = []
    for i in range(len(v1)):
        sums.append((v1[i] - v2[i]) ** 2)
    return sum(sums)


# 文件读取
fhand = open('lena.raw', 'r')
text = fhand.read()
texts = []
for i in text:
    texts.append(ord(i))
fhand.close()
# texts = [randint(0, 255) for i in range(16 * 16)]

# 形成矢量集合
rows = [[] for i in range(512 * 512 / 4)]
for i in range(512 * 512 / 4):
    rows[i] = [texts[4 * i], texts[4 * i + 1], texts[4 * i + 2], texts[4 * i + 3]]

# 读入k值
k = int(raw_input('enter the value of k: '))

# 初始k个中心点
clusters = [[] for i in range(k)]
for i in range(k):
    clusters[i] = [randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255)]

lastmatches = None
for t in range(100):
    bestmatches = [[] for i in range(k)]

    for j in range(len(rows)):
        row = rows[j]
        bestmatch = 0
        for i in range(k):
            d = sim_distance(clusters[i], row)
            if d < sim_distance(clusters[bestmatch], row):
                bestmatch = i
        bestmatches[bestmatch].append(j)
    if bestmatches == lastmatches:
        break
    lastmatches = bestmatches

    # 将中心点移到所有成员的平均位置处
    for i in range(k):
        avgs = [0, 0, 0, 0]
        if len(bestmatches[i]) > 0:
            for rowid in bestmatches[i]:
                for m in range(4):
                    avgs[m] += rows[rowid][m]
            for j in range(len(avgs)):
                avgs[j] /= len(bestmatches[i])
            clusters[i] = avgs

res = []
for i in range(len(rows)):
    for j in range(k):
        if i in bestmatches[j]:
            res.append(j)
            break

# 将数据写入.raw文件
ffhand = open('compress.raw', 'w')
text = ''
for i in res:
    text += str(i) + ','
text = text[: -1]
for i in text:
    ffhand.write(i)
ffhand.write(']')
text = ''
for i in clusters:
    for j in i:
        text += str(j) + ','
text = text[: -1]
for i in text:
    ffhand.write(i)
ffhand.close()