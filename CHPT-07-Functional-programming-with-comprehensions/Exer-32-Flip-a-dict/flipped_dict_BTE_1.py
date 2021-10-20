
'''
Given a string containing several (space-separated) words, create a dict
in which the keys are the words, and the values are the number of vowels
in each word. If the string is “this is an easy test,” then the resulting
dict would be {'this':1, 'is':1, 'an':1, 'easy':2, 'test':1}.
'''

def vwls_cnt_dict(a_str):
    vwls = 'aeuoi'
    return {word:sum([1 if c.lower() in vwls else 0 for c in word])
            for word in a_str.split()}


print(vwls_cnt_dict('this is an easy test,'))
