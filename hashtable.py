"""
description: open addressing Hash Table for CS 141 Lecture
file: hashtable.py
language: python3
author: sps@cs.rit.edu Sean Strout
author: jeh@cs.rit.edu James Heliotis
author: anh@cs.rit.edu Arthur Nunes-Harwitt
author: jsb@cs.rit.edu Jeremy Brown
author: as@cs.rit.edu Amar Saric
"""

"""
modified by Susan Margevich for bieber lab
"""

from rit_lib import *

class HashTable(struct):
    """
           The HashTable data structure contains a collection of values
       where each value is located by a hashable key.
       No two values may have the same key, but more than one
       key may have the same value.
       table is the list holding the hash table
       size is the number of elements in occupying the hashtable

    """
    _slots = ((list, 'table'), (int, 'size'))

def primarySeat(n,capacity):
    """
    multiplies values of letter in a name, mods it with capacity to get primary seat number
    """
    num = 1
    for i in n:
        num *= ord(i) - ord('A') + 1
    return num % capacity

def secondSeat(n,capacity):
    """
    adds values of letter in a name, mods it with capacity to get primary seat number
    """
    num = 0
    for i in n:
        num += ord(i) - ord('A') + 1
    return num % capacity

def createHashTable(capacity=100):
    """
    createHashTable: NatNum? -> HashTable
    """
    if capacity < 2:
        capacity = 2
    aHashTable = HashTable([None for _ in range(capacity)], 0)
    return aHashTable   


def HashTableToStr(hashtable):
    """
    HashTableToStr: HashTable -> String
    """
    result = ""
    for i in range(len(hashtable.table)):
        e = hashtable.table[i]
        if not e == None:
            result += str(i) + ": "
            result += EntryToStr(e) + "\n"
    return result


class Entry(struct):
    """
       A class used to hold key/value pairs.
    """

    _slots = ((object, "key"), (object, "value"))


def EntryToStr(entry):
    """
    EntryToStr: Entry -> String
    return the string representation of the entry.
    """
    return "(" + str(entry.key) + ", " + str(entry.value) + ")"


def hash_function(val, n):
    """
    hash_function: K NatNum -> NatNum
    Compute a hash of the val string that is in [0 ... n).
    """
    hashcode = hash(val) % n
    # hashcode = 0
    # hashcode = len(val) % n
    return hashcode

def keys(hTable):
    """
    keys: HashTable(K, V) -> List(K)
    Return a list of keys in the given hashTable.
    """
    result = []
    for entry in hTable.table:
        if entry != None:
            result.append(entry.key)
    return result

def has(hTable, key):
    """
    determines whether a given key is in the hash table based on the two locations it could reside
    returns boolean True or False
    """
    seat1 = primarySeat(key,len(hTable.table))
    seat2 = secondSeat(key,len(hTable.table))
    if hTable.table[seat1] != None:
        if hTable.table[seat1].key == key:
            return True
    if hTable.table[seat2] != None:
        if hTable.table[seat2].key == key:
            return True
    else:
        return False

def putA(hTable, key, value):
    """
    places new key and value in the table OR updates a key's value based on rules for where it should go
    no return vale
    raises exception if there is a seating error
    """
    seat1 = primarySeat(key,len(hTable.table))
    seat2 = secondSeat(key,len(hTable.table))
    if hTable.table[seat1] == None:
        hTable.table[seat1] = Entry(key, value)
        hTable.size += 1
    else:
        if hTable.table[seat1].key == key:
            hTable.table[seat1] = Entry(key, value)
        else:
            pers = hTable.table[seat1].key
            persval = hTable.table[seat1].value

            if seat2 == secondSeat(pers,len(hTable.table)):
                raise Exception("Could not seat everyone.")

            if seat1 == primarySeat(pers,len(hTable.table)):
                hTable.table[seat1].key = key
                hTable.table[seat1].value = value
                putB(hTable, pers, persval)

def putB(hTable, key, value):
    """
    places new key and value in the table OR updates a key's value based on rules for where it should go
    no return vale
    raises exception if there is a seating error
    works with secondary seat exclusively
    """
    seat2 = secondSeat(key,len(hTable.table))
    if hTable.table[seat2] == None:
        hTable.table[seat2] = Entry(key, value)
        hTable.size += 1
    else:
        if hTable.table[seat2].key == key:
            hTable.table[seat2] = Entry(key, value)
        else:
            pers = hTable.table[seat2].key
            persval = hTable.table[seat2].value

            if seat2 == secondSeat(pers,len(hTable.table)):
                raise Exception("Could not seat everyone.")

            if seat2 == primarySeat(pers,len(hTable.table)):
                hTable.table[seat2].key = key
                hTable.table[seat2].value = value
                putB(hTable, pers, persval)

def get(hTable, key):
    """"
    returns bill of the person associated with the key passed into the function
    """
    seat1 = primarySeat(key, len(hTable.table))
    seat2 = secondSeat(key, len(hTable.table))
    if has(hTable, key) == False:
        return None
    else:
        if hTable.table[seat1].key == key:
            return hTable.table[seat1].value
        elif hTable.table[seat2].key == key:
            return hTable.table[seat2].valye

def indexOf(hTable, key):
    """
    returns seat number of person
    None if person is not seated
    """
    seat1 = primarySeat(key, len(hTable.table))
    seat2 = secondSeat(key, len(hTable.table))
    if has(hTable, key) == False:
        return None
    else:
        if hTable.table[seat1].key == key:
            return seat1
        elif hTable.table[seat2].key == key:
            return seat2
