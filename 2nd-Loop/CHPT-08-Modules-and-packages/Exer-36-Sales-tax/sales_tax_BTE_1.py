'''
Income tax in many countries is not a flat percentage, but rather the
combination of different "brackets." So a country might not tax you on
your first $1,000 of income, and then 10% on the next $10,000, and then
20% on the next $10,000, and then 50% on anything above that. Write a
function that takes someone’s income and returns the amount of tax they
will have to pay, totaling the percentages from various brackets.
'''

brackets = [{'start': 0, 'end': 1000, 'tax': 0},
            {'start': 1000, 'end': 10000, 'tax': .1},
            {'start': 10000, 'end': 20000, 'tax': .2},
            {'start': 20000, 'end': 999999999999, 'tax': .5}]

def tax_brackets(amount, brackets):
    tax_owed = 0

    for one_bracket in brackets:
        if amount < one_bracket['start']:
            continue

        taxed_amount = min(amount, one_bracket['end'])
        taxed_amount -= one_bracket['start']

        tax_owed += taxed_amount * one_bracket['tax']
    return tax_owed










        


