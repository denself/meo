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
for alt in range(number_of_alternatives):
    results.append([None] * number_of_experts)
    for exp in range(number_of_experts):
        val = raw_input("Expert {}, give your rating to alternative {}:\n"
                        ">>> ".format(experts[exp], alternatives[alt]))
        results[alt][exp] = int(val)

print "Original results"
table = Texttable()
table.add_rows([['Alternatives']+experts])
table.add_rows(results, header=False)
print(table.draw())