
def plword(word):
    if word[0] in 'aeiou':
        return word + 'way'
    return word[1:] + word[0] + 'ay'

def plfile(fname):
    return ' '.join(plword(one_word)
      for one_line in open(fname)
      for one_word in one_line.split())
    
print(plfile('sonnet_126.txt'))
