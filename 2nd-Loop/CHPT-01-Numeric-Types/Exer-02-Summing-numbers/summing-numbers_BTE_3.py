'''
Write a function that takes a list of words (strings). It should return a tuple containing three integers,
representing the length of the shortest word, the length of the longest word, and the average word length.
'''
def word_stats(li):
    word_len = []
    for item in li:
        word_len.append( (len(item), item) )

    word_len.sort()
    avg_word_len = 0

    for num in word_len:
        avg_word_len += num[0]

    avg_word_len = avg_word_len // len(word_len)

    print(f"Longest word: {word_len[-1][1]}")
    print(f"\nShortest word: {word_len[0][1]}")
    print(f"Length of the shortest word: {word_len[0][0]}")
    print()
    print(f"The average word length is: ", avg_word_len)
    print()
    print(f"({word_len[0][0]}, {word_len[-1][0]}, {avg_word_len})")
 
word_stats(["Py", "Python", "Exercises"])
