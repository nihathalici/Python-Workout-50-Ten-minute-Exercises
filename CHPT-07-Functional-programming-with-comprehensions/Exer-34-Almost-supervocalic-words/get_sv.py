def get_sv(fname):
    vwls = {'a', 'e', 'i', 'o', 'u'}

    return {word
            for word in open(fname)
            if vwls <= set( word.lower() ) }

print(get_sv('words.txt'))
    
