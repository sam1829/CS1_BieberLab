
"""
prompts user for size of hashtable and runs seating simulation
author: Susan Margevich
file: bieberhash.py
"""

from hashtable import *

def create_bills(filename, capacity):
    """
    creates hash table
    opens inputted file, reads and updates hash table with names and tabs
    checks to see if all attendees could be seated or not
    """
    hashT = createHashTable(capacity)
    file = open(filename)
    for line in file:
        line = line.split()
        pers = line[0].upper()
        tab = int(line[1][1:])
        seat1 = primarySeat(pers, capacity)
        seat2 = secondSeat(pers, capacity)

        if has(hashT, pers):
            y = get(hashT, pers)
            index = indexOf(hashT, pers)
            if index == seat1:
                putA(hashT, pers, tab + y)
            if index == seat2:
                putB(hashT, pers, tab + y)
        else:
            putA(hashT, pers, tab)
    for q in range(0, capacity):
        if hashT.table[q] == None:
            pass
        else:
            key = hashT.table[q].key
            print(key, "owes $ ", get(hashT, key), "and is in seat ", indexOf(hashT, key))

def main():
    size = int(input("How big a hashtable to use: "))
    filename = input("Name of input file: ")
    create_bills(filename, size)

main()

