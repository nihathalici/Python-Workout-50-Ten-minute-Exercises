
'''
Take a text file, creating (and printing) a nonsensical sentence from the nth
word on each of the first 10 lines, where n is the line number.
'''

N = int(input("Take a number between 0 - 5: "))

st_nouns = "puppy car rabbit girl monkey"
st_verbs = "runs hits jumps drives barfs"
st_adv = "crazily dutifully foolishly merrily occasionally"
st_adj = "adorable clueless dirty odd stupid"

nouns_tup = tuple(st_nouns.split(' '))
verbs_tup = tuple(st_verbs.split(' '))
adv_tup = tuple(st_adv.split(' '))
adj_tup = tuple(st_adj.split(' '))

print(nouns_tup[N].capitalize() + ' ' + verbs_tup[N] + ' ' + adv_tup[N] + ' ' + adj_tup[N]  + '.')