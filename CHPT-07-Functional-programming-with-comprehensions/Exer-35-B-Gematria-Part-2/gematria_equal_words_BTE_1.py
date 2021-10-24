'''
Create a dict whose keys are city names, and whose values are temperatures in
Fahrenheit. Now use a dict comprehension to transform this dict into a new one,
keeping the old keys but turning the values into the temperature in degrees Celsius.
'''

fahr_temp_di = {'Lisbon, Portugal':69, 'Stockholm, Sweden':36,
                'Warsaw, Poland':41, 'Germany, Berlin':46} 

def conv_to_cels():
    return { key:round( (val - 32) * (5/9) )
            for key, val in fahr_temp_di.items() }

print(conv_to_cels())
