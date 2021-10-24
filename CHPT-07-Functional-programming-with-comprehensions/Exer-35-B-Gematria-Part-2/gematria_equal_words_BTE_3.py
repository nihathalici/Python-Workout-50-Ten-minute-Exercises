'''
Create a dict whose keys are currency names and whose values are the price of that currency
in U.S. dollars. Write a function that asks the user what currency they use, then returns
the dict from the previous exercise as before, but with its prices converted into the requested currency.
'''


def con_val():
    d = {'lt':0.28, 'us':0.83}
    value = input('Enter price and currency, to translate it to euros: ')
    cur_name = value.lower().strip().split()[-1]
    cur_price = value.strip().split()[0]
    return round( int(cur_price) * d.get(cur_name, 2)) if d.get(cur_name, 0) else 'Currency unknown'


print(con_val())
    
