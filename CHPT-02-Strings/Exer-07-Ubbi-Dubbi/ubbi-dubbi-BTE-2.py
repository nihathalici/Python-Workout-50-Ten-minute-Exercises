
"""
Remove author names—In academia, it’s common to remove the authors’ names
from a paper submitted for peer review. Given a string containing an article and
a separate list of strings containing authors’ names, replace all names in the
article with _ characters.
"""

def rem_auth_name(text, auth_lst):
    for auth_name in auth_lst:
        if auth_name in text:
            # alternative method:
            # text = text.replace(auth_name, auth_name[0]+'_'*len(auth_name))
            # the first character of the name is printed. Sample output:
            # Author of this article is A____________.
            text = text.replace(auth_name, '_'*len(auth_name))
    return text

my_text = "Author of this article is Ada Lovelace.\nSecond author of the article is Marie Curie'"
my_auth_lst = ['Ada Lovelace', 'Marie Curie']

print(rem_auth_name(my_text, my_auth_lst))

"""
Output:
Author of this article is ____________.
Second author of the article is ___________'
"""
