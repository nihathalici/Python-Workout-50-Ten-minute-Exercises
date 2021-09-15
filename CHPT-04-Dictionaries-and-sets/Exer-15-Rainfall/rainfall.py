
def get_rainfall():
    rainfall = {}

    while True:
        city_name = input("Enter city name: ").strip()

        if not city_name:
            break

        mm_rain = input("Enter mm rain: ")
        rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)

    for key, value in rainfall.items():
        print(f'{key}: {value}')

get_rainfall()
