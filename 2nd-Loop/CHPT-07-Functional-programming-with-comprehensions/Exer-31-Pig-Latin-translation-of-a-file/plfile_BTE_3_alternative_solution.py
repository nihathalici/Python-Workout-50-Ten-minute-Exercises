
'''
Assume that you have a list of dicts, in which each dict contains two name-value pairs:
name and hobbies, where name is the person’s name and hobbies is a set of strings
representing the person’s hobbies. What are the three most popular hobbies among the
people listed in the dicts?
'''

from collections import Counter

hby_di_lst = [{'Nm':'Mary','Hby':set(['reading', 'collecting', 'fishing', 'traveling'])},
              {'Nm':'Linda','Hby':set(['reading', 'collecting', 'gardening', 'traveling'])},
              {'Nm':'James','Hby':set(['reading', 'collecting', 'fishing', 'traveling'])},
              {'Nm':'John','Hby':set(['reading', 'collecting', 'walking'])},]

def mst_pp_thr_hby():
    cnt_obj = Counter(k for di_item in hby_di_lst for k in di_item['Hby'])
    print(cnt_obj.most_common(3))

print(mst_pp_thr_hby())
