
'''
Define a dict whose keys are names of people in your family, and whose values
are their birth dates, as represented by Python date objects (http://mng.bz/jggr).
Ask the user to enter the name of someone in your family, and have the program
calculate how many days old that person is.
'''


from datetime import date

def bday_chq():
    BDAYS = {'Ada': date(1815,12,10), 'Alan': date(1912,6,23), 'Unix':date(1970,1,1), 'Linux':date(1991,8,25)}
    name_inp = input(f'Enter name {list(BDAYS.keys())}: ')
    cur_days_old = 0
    cur_years_old = 0

    if name_inp in BDAYS:
        cur_days_old = (date.today() - BDAYS[name_inp]).days
        cur_years_old = (date.today() - BDAYS[name_inp]).days // 365

    print(f'{name_inp} is {cur_days_old} days old. That is {cur_years_old} years.')

bday_chq()
