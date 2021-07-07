"""
DNA_nuc:four kinds of DNA (Deoxyribonucleic Acid) nucleobases
notice:in this program,a person has only 4600 nucleobases!
"""

import random as r
import time as t

a = t.perf_counter()
DNA_nuc = ["A", "G", "C", "T"]
def string(list):
    s = ""
    for i in list:
        for j in i:
            s += j
        s += "\n\t\t\t"
    return s

def rand_chromosome():
    dna = []
    for i in range(100):
        dna.append(DNA_nuc[r.randint(0, 3)])
    return dna

class DNA:
    def __init__(self):
        self.dna1 = []
        for i in range(23):
            self.dna1.append(rand_chromosome())
        self.dna2 = []
        for i in range(23):
            self.dna2.append(rand_chromosome())
        self.dna = [self.dna1, self.dna2]

    def index(self, num):
        return self.dna[num]

class Person:
    def __init__(self, dna):
        self.dna = dna

    def child_dna(self):
        return self.dna[r.randint(0, 1)]
people = []

def __main__(contemporary):
    if contemporary == 1:
        people.append([Person([people[-1][0].child_dna, people[-1][1].child_dna])])
    else:
        p = []
        for i in range(2**contemporary):
            p.append(Person([people[-1][2*i-2].child_dna(), people[-1][2*i-1].child_dna()]))
        people.append(p)
        __main__(contemporary-1)

contem = int(input("how many contemporaries?(>1)"))
p = []
print('<?xml version="1.0" encoding="UTF-8"?>\n<doc>\n\t<ancestor>')
for i in range(2**contem):
    dna = DNA().dna
    p.append(Person(dna))
    print("\t\t<person>\n\t\t\t"+string(dna[0])+",\n\t\t\t"+string(dna[1])+"\n\t\t</person>")
people.append(p)
print("\t</ancestor>")
__main__(contem-1)
for i in people[0:-1]:
    print('\t<posterity num="'+str(people.index(i))+'">')
    for j in i:
        print("\t\t<person>\n\t\t\t"+string(j.dna[0])+","+string(j.dna[1])+"\n\t\t</person>")
    print("\t</posterity>")
print("</doc>")
b = t.perf_counter()
print("time:"+str(b-a)+"s")
