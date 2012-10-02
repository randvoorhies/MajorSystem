#!/usr/bin/env python

import pprint

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

majorsystem = {
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

NOUN = 'n'
ADJ = 'j'

######################################################################
def read_word_frequencies(filename):
  with open(filename, 'r') as f:
    lines = f.read().split('\n')

    # Filter out lines that don't start with 0-9
    lines = filter(lambda x: len(x) and ord(x[0]) > 47 and ord(x[0]) < 58 , lines)

    words = {}
    for line in lines:
      s = line.split('\t')

      words[s[1]] = {
          'rank' : s[0],
          'PoS'  : s[2]
          }

    return words

######################################################################
def read_pronunciation(filename):
  with open(filename, 'r') as f:

    lines = f.read().split('\n')

    # Filter out lines that don't start with A-Z
    lines = filter(lambda x: len(x) and ord(x[0]) > 64 and ord(x[0]) < 91 , lines)

    # Filter out lines that have an apostrophe in them
    lines = filter(lambda x: x.count("'") == 0 and x.count("(") == 0, lines)

    words = {}
    for line in lines:
      i = line.find(' ')
      word = line[:i].lower()

      pronunciation = line[i:].strip().split(' ')
      words[word] = [p.strip('0123456789') for p in pronunciation]

    return words

######################################################################
def get_words():
  pronunciations  = read_pronunciation('cmudict.0.7a.txt')

  words = {}
  for word in pronunciations:
    # Make sure we don't have any unassigned phonemes
    if any(x in unassigned for x in pronunciations[word]): continue

    # Make sure the word has at least one assigned consanant in it.
    if not any(x in consonants for x in pronunciations[word]): continue

    words[word] = {}
    words[word]['pronunciation'] = pronunciations[word]
  return words

  #word_frequencies = read_word_frequencies('wordfrequencies.txt')

  #words = {}
  #for word in word_frequencies:

  #  # Make sure we have a pronunciation for this word
  #  if pronunciations.has_key(word):
  #    pronunciation = pronunciations[word]

  #    # If the pronunciation doesn't have any unassigned phonemes in it, then
  #    # let's stick it in the word list
  #    if not any(x in unassigned for x in pronunciation):
  #      words[word] = word_frequencies[word]
  #      words[word]['pronunciation'] = pronunciation

  #return words

######################################################################
def eat_word(nums, word):
  i = 0
  for p in word['pronunciation']:

    # If we have more phenomes than numbers, then bail out.
    if i >= len(nums):
      return None

    if p in vowels:
      continue
    elif p in majorsystem[nums[i]]:
      i += 1
    else :
      return None

  return i

######################################################################
def find_sequence(nums, words):
  working_sequences = []
  final_sequences = []

  for word in words:
    index = eat_word(nums, words[word])
    if index is not None:
      working_sequences.append(
          {
            'words' : [word],
            'index' : index
          }
        )

  curr_sequences = []
  while len(working_sequences) > 0:
    print '-------------'

    for sequence in working_sequences:
      for word in words:
        index = eat_word(nums[sequence['index']:], words[word])

        if index is not None:
          print 'Sequence: ', sequence, '[', word, '] index=', index
          sequence['index'] += index
          sequence['words'] += word
          if index == len(nums):
            final_sequences.append(sequence)
          else:
            curr_sequences.append(sequence)

    working_sequences = curr_sequences


  return working_sequences

#words = get_words()
#print words['bob']
#sequences = find_sequence([9, 9], words)
#pprint.pprint(sequences)
