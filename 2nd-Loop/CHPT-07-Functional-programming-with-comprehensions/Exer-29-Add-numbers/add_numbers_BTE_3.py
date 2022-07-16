
'''
Define a list of five dicts. Each dict will have two key-value pairs, name and age,
containing a person’s name and age (in years). Use a list comprehension to produce
a list of dicts in which each dict contains three key-value pairs: the original name,
the original age, and a third age_in_months key, containing the person’s age in months.
However, the output should exclude any of the input dicts representing people over 20 years of age.
'''


def ages_dict(lst_of_person):
    new_lst = [ {**d, **{'age_in_months':d['age']*12}} for d in lst_of_person]
    return list(filter(lambda x: x['age'] > 20, new_lst))


my_person_list = [{'name':'James','age':10},{'name':'John','age':32},{'name':'Mary','age':17},{'name':'Linda','age':24}]

print(ages_dict( my_person_list ))

###

def ages_dict(lst_of_person):
    new_lst = [{**d, **{'age_in_months': d['age']*12}} for d in lst_of_person]
    return list(filter(lambda x: x['age'] > 20, new_lst))

my_person_list = [{'name':'James','age':10},{'name':'John','age':32},{'name':'Mary','age':17},{'name':'Linda','age':24}]
print(ages_dict( my_person_list ))
