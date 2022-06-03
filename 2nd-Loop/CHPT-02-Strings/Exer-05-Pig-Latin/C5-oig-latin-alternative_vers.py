'''
Consider an alternative version of Pig Latin—We don’t check to see if the first letter is a vowel,
but, rather, we check to see if the word contains two different vowels. If it does, we don’t move
the first letter to the end.

Because the word “wine” contains two different vowels (“i” and “e”), we’ll add “way” to the end
of it, giving us “wineway.” By contrast, the word “wind” contains only one vowel, so we would move
the first letter to the end and add “ay,” rendering it “indway.”

How would you check for two different vowels in the word? (Hint: sets can come in handy here.)
'''


def pig_latin(word):
    final_string = ''
    vow_nums = 0
    set_word = set(word)

    for ch in set_word:
        if ch in 'aeiou':
            vow_nums += 1

    if vow_nums >= 2:
        final_string = word + "way"
        return final_string.capitalize()
    elif vow_nums < 2:
        final_string = word[1:] + word[:1] + 'ay'
        return final_string.capitalize()

print(pig_latin('wine'))
print(pig_latin('wind'))


