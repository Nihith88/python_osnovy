"""
6.1. итератор, повторяющий элементы некоторого списка, определённого заранее.
"""

from sys import argv
import itertools

script_name, total_count = argv

rules = ['стеклянный', 'оловянный', 'деревянный']
rule = itertools.cycle(rules)
for i in range(1, int(total_count)+1):
    print(next(rule))
