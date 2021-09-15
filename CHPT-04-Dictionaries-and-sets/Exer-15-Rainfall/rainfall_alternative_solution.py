
def get_rainfall():
    rainfall = {}

    while True:
        cname = input("Enter the city: ")
        if not cname:
            print("No entry. Displaying the results:")
            break
        rain_val = input("Enter in mm:")
        rainfall[cname] = rainfall.get(cname, 0) + int(rain_val)

    for k, v in rainfall.items():
        print("{0:5} : {1:5}".format(k, v))

get_rainfall()
