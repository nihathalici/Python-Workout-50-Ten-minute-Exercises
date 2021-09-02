
'''
Handle capitalized words—If a word is capitalized (i.e., the first letter is capitalized,
but the rest of the word isn’t), then the Ubbi Dubbi translation should be similarly capitalized.
'''

def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
            if word.isupper():
                word.isupper()
        else:
            output.append(letter)

    return ''.join(output)

print(ubbi_dubbi('python'))
