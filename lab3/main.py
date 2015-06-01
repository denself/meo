# -*- coding: utf-8 -*-
from lab2.main import gurvits_func, laplas_func, vald_func, sevidj_func
import csv
from texttable import Texttable

__author__ = 'Denis Ivanets (denself@gmail.com)'

# I don't know which functions should I use to compere alternatives, so I used
# cryterias from prev lab
lpr = gurvits_func, laplas_func, vald_func, sevidj_func

with open('input.csv') as csv_file:
    stream_reader = csv.reader(csv_file, delimiter=',')
    matrix = []
    names = []
    for row in stream_reader:
        name = row[0]
        names.append(name)
        params = [float(i) for i in row[1:]]
        matrix.append(params)

n = len(matrix)
results_matrix = [[0]*n for i in range(n)]

for j in range(n-1):
    for i in range(j+1, n):
        row1 = matrix[i]
        row2 = matrix[j]
        score = [0, 0]
        for func in lpr:
            score[func([row1, row2])[2]] += 1
        if score[0] != score[1]:
            bigger = (i, j)[score.index(max(score))]
            smaller = (i, j)[score.index(min(score))]
            results_matrix[smaller][bigger] = 1

table = Texttable(max_width=150)
table.set_deco(Texttable.HEADER)
table.set_precision(1)
table.add_rows([['']+names])
for i in range(n):
    table.add_rows([[names[i]]+results_matrix[i]], header=False)
print table.draw()

print 'Best solutions:',
for i in range(n):
    if max(zip(*results_matrix)[i]) == 0:
        print names[i],