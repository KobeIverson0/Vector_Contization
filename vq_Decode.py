#!/usr/bin/python
# coding:utf-8

fhand = open('compress.raw', 'r')
text = fhand.read()
fhand.close()

index = text.find(']')
text_1 = text[: index]
text_2 = text[index + 1: ]

text_1 = text_1.split(',')
text_2 = text_2.split(',')
text1 = []
for i in text_1:
    text1.append(int(i))
text2 = []
for i in text_2:
    text2.append(int(i))

length = len(text2)
clusters = [[] for i in range(length / 4)]
for i in range(len(clusters)):
    a = text2[4 * i: 4 * i + 4]
    clusters[i] = a

lena = []
for i in text1:
    for j in range(4):
        lena.append(clusters[i][j])

res = ''
for i in lena:
    res += chr(i)

ffhand = open('restore.raw', 'w')
ffhand.write(res)
ffhand.close()
