
'''
It’s sometimes useful to transform data from one format into another. Download a JSON-formatted
list of the 1,000 largest cities in the United States from http://mng.bz/Vgd0. Using a dict
comprehension, turn it into a dict in which the keys are the city names, and the values are
the populations of those cities. Why are there only 925 key-value pairs in this dict? Now
create a new dict, but set each key to be a tuple containing the state and city. Does that
ensure there will be 1,000 key-value pairs?
'''

import json

def crt_dct_jsn(a_file):
    di = {}
    with open(a_file) as f:
        jsn_obj = json.load(f)
        di = { (item['city']) : item['population']
               for item in jsn_obj }
        return di




print(crt_dct_jsn('cities.json'))


