
def wcount(fname):

    cnts = {'characters': 0,
              'words': 0,
              'lines': 0}
    unq_wo = set()

    for one_line in open(fname):
        cnts['lines'] += 1
        cnts['characters'] += len(one_line)
        cnts['words'] += len(one_line.split())

        unq_wo.update(one_line.split())

    cnts['unique words'] = len(unq_wo)

    for k, v in cnts.items():
        print(f'{k}: {v}')

wcount('wcountfile.txt')
