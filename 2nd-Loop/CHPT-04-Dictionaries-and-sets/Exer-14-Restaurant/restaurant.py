
MENU = {'sandwich':10, 'tea':7, 'salad':9}

def restaurant():

    total = 0
    while True:
        order = input("Enter your order: ").strip()

        if not order:
            break

        if order in MENU:
            price = MENU[order]
            total += int(price)
            print(f'{order} costs {price}, total is now {total}')

        else:
            print(f'We are fresh out of {order} today.')
    print(f'Your total is {total}')

restaurant()
