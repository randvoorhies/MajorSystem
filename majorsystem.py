#!/usr/bin/env python

def read_dict(filename):
  with open(filename, 'r') as f:

    lines = f.read().split('\n')

     # Filter out lines that don't start with A-Z
    lines = filter(lambda x: len(x) and ord(x[0]) > 64 and ord(x[0]) < 91 , lines)

    dictionary = dict((line[:line.find(' ')], line[line.find(' '):].strip().split(' ')) for line in lines)

    return dictionary

dictionary = read_dict('cmudict.0.7a.txt')

for d in dictionary:
  print d, dictionary[d]
