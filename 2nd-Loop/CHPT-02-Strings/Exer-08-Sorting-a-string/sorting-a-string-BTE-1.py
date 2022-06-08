
'''
Given the string “Tom Dick Harry,” break it into individual words,
and then sort those words alphabetically. Once they’re sorted, print them
with commas (,) between the names.
'''

s = "Tom Dick Harry"

splitted_and_sorted = sorted(s.split())

result = ', '.join(splitted_and_sorted)

print(result)
