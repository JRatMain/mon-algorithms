import csv
import time
import re

mons = []


def max_total(reader):
    global mons
    max = 0
    for row in mons:
        num = row[0]
        name = row[1]
        t1 = row[2]
        t2 = row[3]
        total = row[4]
        hp = row[5]
        atk = row[6]
        defense = row[7]
        spatk = row[8]
        spdef = row[9]
        spd = row[10]
        gen = row[11]
        legend = bool(row[12])



def check_type_psn(reader):
    global mons
    print("The following Pokémon have the Poison type: ")
    print()
    for row in reader:
        t1 = row[2]
        t2 = row[3]
        legend = bool(row[12])
        if t1 == 'Poison' or t2 == 'Poison':
            print(row[1])
        mons.append(row)


with open('Pokemon_numerical.csv') as mon:
    if __name__ == '__main__':
        reader = csv.reader(mon)
        check_type_psn(reader)
        max_total(reader)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
