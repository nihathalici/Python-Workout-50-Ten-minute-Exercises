
def wcount(fname):
    cnts = {'characters': 0,
            'words': 0,
            'lines': 0}
    unq_wo = set()
    for x in open(fname):
        cnts['lines'] += 1
        cnts['characters'] += len(x)
        cnts['words'] += len(x.split())
        unq_wo.update(x.split())
    print(unq_wo)
    cnts['unique words'] = len(unq_wo)
    for k, v in cnts.items():
        print(f'{k}: {v}')
        
wcount('wcountfile.txt')            
