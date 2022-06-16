'''
Define a dict whose keys are dates (represented by strings) from the most recent week
and whose values are temperatures. Ask the user to enter a date, and display the
temperature on that date, as well as the previous and subsequent dates, if available.
'''

def temp_check():
    DT = {'06/09': '20', '07/09': '21', '08/09': '23', '09/09': '24',
          '10/09': '23', '11/09': '23', '12/09': '27'}

    dt_inp = input('Please enter date in "dd/mm" format, between 06/09 - 12/09: ')
    if dt_inp in DT:
        ks_li = list(DT.keys())
        pr_day = ks_li[ks_li.index(dt_inp) - 1] if (ks_li.index(dt_inp) - 1) >= 0 else ''
        nx_day = ks_li[ks_li.index(dt_inp) + 1] if (ks_li.index(dt_inp) + 1) < len(ks_li) else ''

        print(f'TEMPERATURE LIST:\nPrevious day: {DT.get(pr_day, "N.A.")}')
        print(f'Chosen day: {DT.get(dt_inp)}')
        print(f'Next day: {DT.get(nx_day, "N.A.")}')
    else:
        print('Please try again')

temp_check()          
    
