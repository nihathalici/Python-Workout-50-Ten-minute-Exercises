'''
Given a text file, what are the lengths of the different words?
Return a set of different word lengths in the file.
'''

def wo_lngth(a_file):
    return {len(wrd.strip())
            for wrd in open(a_file)}

print(wo_lngth('words.txt'))

