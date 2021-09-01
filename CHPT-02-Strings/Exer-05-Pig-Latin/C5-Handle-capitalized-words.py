'''
Handle capitalized words—If a word is capitalized (i.e., the first letter is capitalized,
but the rest of the word isn’t), then the Pig Latin translation should be similarly capitalized.
'''

def pig_latin(word):
    final_string = ''
    if word[0] in 'aeiou':
        final_string = word + 'way'
        return final_string.capitalize()
    else:
        final_string = word[1:] + word[:1] + 'ay'
        return final_string.capitalize()

print(pig_latin('python'))
