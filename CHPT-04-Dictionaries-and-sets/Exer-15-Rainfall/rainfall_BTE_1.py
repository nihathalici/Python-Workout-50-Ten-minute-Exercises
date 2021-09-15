
'''
Instead of printing just the total rainfall for each city, print the total
rainfall and the average rainfall for reported days. Thus, if you were to
enter 30, 20, and 40 for Boston, you would see that the total was 90
and the average was 30.
'''

def rainfall_stats():
    ch = 1
    dict_rain = {}

    while ch:
        ch = input('Enter city: ')
        if not ch:
            continue

        rainfall = int(input('Rainfall in mm '))
        dict_rain[ch] = (dict_rain.get(ch, (0, 0))[0] + rainfall, dict_rain.get(ch, (0, 0))[1] + 1)
    else:
        for k, v in dict_rain.items():
            print(f'For {k} the total rainfall is: {v[0]}, the average rainfall: {v[0]//v[1]}')


rainfall_stats()
