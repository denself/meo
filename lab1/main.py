# -*- coding: utf-8 -*-
from texttable import Texttable

__author__ = 'Denis Ivanets (denself@gmail.com)'

number_of_alternatives = raw_input("Please, enter number of alternatives:\n>>> ")
number_of_alternatives = int(number_of_alternatives)

alternatives = [None] * number_of_alternatives
for i in range(number_of_alternatives):
    alternatives[i] = raw_input('Enter name of alternative #{}:\n>>> '.format(i+1))

number_of_experts = raw_input("Please, enter number of experts:\n>>> ")

number_of_experts = int(number_of_experts)
experts = [None] * number_of_experts
for i in range(number_of_experts):
    experts[i] = raw_input('Enter name of expert #{}:\n>>> '.format(i+1))

min_rating = raw_input("Please, enter minimal rating value:\n>>> ")
min_rating = int(min_rating)

max_rating = raw_input("Please, enter maximum rating value:\n>>> ")
max_rating = int(max_rating)

results = []
for exp in range(number_of_experts):
    results.append([None] * number_of_alternatives)
    for alt in range(number_of_alternatives):
        val = raw_input("Expert {}, give your rating to alternative {}:\n"
                        ">>> ".format(experts[exp], alternatives[alt]))
        results[exp][alt] = int(val)


alternatives_summary = [None] * number_of_experts
for exp in range(number_of_experts):
    alternatives_summary[exp] = sum(results[exp])

normalized_rating = [None] * number_of_alternatives
for alt in range(number_of_alternatives):
    value = 0
    for exp in range(number_of_experts):
        value += results[exp][alt] / float(alternatives_summary[exp])
    value /= number_of_experts
    normalized_rating[alt] = value


print "Results"
table = Texttable()
table.add_rows([['Experts'] + alternatives + ['Summary']])
table.add_rows([[experts[row]] + results[row] + [alternatives_summary[row]] for row in range(number_of_experts)], header=False)
table.add_rows([['Normalized'] + normalized_rating + ['']], header=False)

print(table.draw())

print
print 'Rearranged results'
table = Texttable()
table.add_rows([['Alternative name', 'Normalized rating']])
table.add_rows(sorted(zip(alternatives, normalized_rating), key=lambda x:x[1], reverse=True), header=False)
print(table.draw())