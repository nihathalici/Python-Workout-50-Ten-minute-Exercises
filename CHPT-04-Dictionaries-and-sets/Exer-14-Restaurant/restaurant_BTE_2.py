'''
Define a dict whose keys are dates (represented by strings) from the most recent week
and whose values are temperatures. Ask the user to enter a date, and display the
temperature on that date, as well as the previous and subsequent dates, if available.
'''

def dates_temp():
    DATES = {'07/03':'1', '08/03':'2', '09/03':'-1', '10/03':'10', '11/03':'-5','12/03':'1','13/03':'0'}
    choice = input('Enter date to see the weather in format "dd/mm": ')
    if choice in DATES:
        dict_keys = list(DATES.keys())
        prevd = dict_keys[dict_keys.index(choice) -1] if (dict_keys.index(choice) -1) >=0 else ''
        nextd = dict_keys[dict_keys.index(choice) + 1] if (dict_keys.index(choice) + 1) < len(dict_keys) else ''

        # print(str(dict_keys[prevd:prevd+1]),str(dict_keys[nextd:nextd+1]))
        print(f'Temperature of previouse day, chosen day, next day: {DATES.get(prevd, "NOT AVAILABLE")},{DATES.get(choice)},{DATES.get(nextd,"NOT AVAILABLE")}')
    else:
        print('Either entered wrong format or such date does not exists in previouse week.')
