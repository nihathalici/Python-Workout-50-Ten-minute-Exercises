'''
Read through a text file on disk. Use a dict to track how many words
of each length are in the file—that is, how many three-letter words,
four-letter words, five-letter words, and so on. Display your results.
'''

def file_chq(fname):
    sym = ['.',',','?','!','\n']
    wo_li = {}
    with open(fname, 'r') as f:
        for l in f:
            for c in sym:
                l = l.replace(c, '')
            l = l.split()
            for wo in l:
                wo_li[len(wo)] = wo_li.get(len(wo), 0) + 1
    for nr in wo_li:
        print(f'The file contains {wo_li[nr]} words with {nr} letters.')


file_chq('txt_file.txt')

