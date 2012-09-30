#!/usr/bin/env python

vowels = [
'AA',
'AE',
'AH',
'AO',
'AW',
'AY',
'EH',
'EY',
'IH',
'IY',
'OW',
'OY',
'UH',
'UW']

unassigned = [
  'DH',
  'HH',
  'JH',
  'NG',
  'TH',
  'W',
  'Y']

consonants = [
  'B',
  'CH',
  'D',
  'ER',
  'F',
  'G',
  'K',
  'L',
  'M',
  'N',
  'P',
  'R',
  'S',
  'SH',
  'T',
  'V',
  'Z',
  'ZH']

major_system = {
    0 : ['S', 'Z'],
    1 : ['T', 'D'],
    2 : ['N'],
    3 : ['M'],
    4 : ['R', 'ER'],
    5 : ['L'],
    6 : ['SH', 'CH', 'ZH'],
    7 : ['K', 'G'],
    8 : ['F', 'V'],
    9 : ['P', 'B']
    }

def read_word_frequencies(filename):
  with open(filename, 'r') as f:
    lines = f.read().split('\n')

    # Filter out lines that don't start with 0-9
    lines = filter(lambda x: len(x) and ord(x[0]) > 47 and ord(x[0]) < 58 , lines)

    adjectives = {}
    nouns = {}
    for line in lines:
      s = line.split('\t')
      rank = s[0]
      word = s[1]
      PoS  = s[2]

      # adjectives
      if PoS == 'j':
        adjectives[word] = rank
      # noun
      elif PoS == 'n':
        nouns[word] = rank

    return {'adjectives' : adjectives, 'nouns' : nouns}

def read_pronunciation(filename):
  with open(filename, 'r') as f:

    lines = f.read().split('\n')

     # Filter out lines that don't start with A-Z
    lines = filter(lambda x: len(x) and ord(x[0]) > 64 and ord(x[0]) < 91 , lines)

    # Filter out lines that have an apostrophe in them
    lines = filter(lambda x: x.count("'") == 0 and x.count("(") == 0, lines)

    # Return the words as a dictionary with the word as the key, and an array of the phonemes as the value
    return dict((line[:line.find(' ')].lower(), line[line.find(' '):].strip().split(' ')) for line in lines)

def get_words():
  pronunciations = read_pronunciation('cmudict.0.7a.txt')

  word_frequencies = read_word_frequencies('wordfrequencies.txt')

get_words()
