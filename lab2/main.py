# -*- coding: utf-8 -*-
import csv
from texttable import Texttable

__author__ = 'Denis Ivanets (denself@gmail.com)'

def laplas_func(matrix):
    coef = 1./len(matrix[0])
    results = [sum(map(lambda x: x*coef, params)) for params in matrix]
    return results, max(results), results.index(max(results))


def vald_func(matrix):
    results = map(min, matrix)
    return results, max(results), results.index(max(results))


def minmax_func(matrix):
    results = map(max, matrix)
    return results, min(results), results.index(min(results))

def sevidj_func(matrix):
    r_matrix = zip(*matrix)
    max_r = map(max, r_matrix)
    r_new_matrix = map(lambda x, y: [x-yi for yi in y], max_r, r_matrix)
    new_matrix = zip(*r_new_matrix)
    results = map(max, new_matrix)
    return results, min(results), results.index(min(results))


def gurvits_func(matrix):
    y = 0.5
    results = map(lambda x: y*min(x)+(1-y)*(max(x)), matrix)
    return results, max(results), results.index(max(results))

with open('input.csv') as csv_file:
    stream_reader = csv.reader(csv_file, delimiter=',')
    matrix = []
    names = []
    for row in stream_reader:
        name = row[0]
        names.append(name)
        params = [float(i) for i in row[1:]]
        matrix.append(params)
vald = vald_func(matrix)
minmax = minmax_func(matrix)
gurvits = gurvits_func(matrix)
sevidj = sevidj_func(matrix)
laplas = laplas_func(matrix)

table = Texttable(max_width=150)
table.set_deco(Texttable.HEADER)
table.set_precision(1)
table.add_rows([['Actions'] + ['p{}'.format(i) for i in range(len(matrix[0]))] + ['Vald', 'Minmax', 'Gurvits', 'Sevidj', 'Laplas']])
for i in range(len(matrix)):
    v = ('!{}!' if i == vald[2] else '{}').format(vald[0][i])
    m = ('!{}!' if i == minmax[2] else '{}').format(minmax[0][i])
    g = ('!{}!' if i == gurvits[2] else '{}').format(gurvits[0][i])
    s = ('!{}!' if i == sevidj[2] else '{}').format(sevidj[0][i])
    l = ('!{}!' if i == laplas[2] else '{}').format(laplas[0][i])
    table.add_rows([[names[i]]+matrix[i] + [v, m, g, s, l]], header=False)

print(table.draw())