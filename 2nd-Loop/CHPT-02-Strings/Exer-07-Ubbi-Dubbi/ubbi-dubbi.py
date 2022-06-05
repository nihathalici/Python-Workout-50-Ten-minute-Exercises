
def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)

    return ''.join(output)

print(ubbi_dubbi('python'))
