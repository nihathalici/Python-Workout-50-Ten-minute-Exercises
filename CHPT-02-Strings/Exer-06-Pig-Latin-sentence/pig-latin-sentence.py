
def pl_sentence(sentence):
    output = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')

    return ' '.join(output)

print(pl_sentence('this is a test'))

            

    
