'''
Write a function that takes a float and two integers (before and after).
The function should return a float consisting of before digits
before the decimal point and after digits after. Thus, if we call
the function with 1234.5678, 2 and 3, the return value should be 34.567.
'''

def cropNumber(fl_num, bef_int_num, aft_int_num):
    # Digits before decimal point 
    str_bef = str(int(fl_num))
    str_bef = str_bef[-bef_int_num:]
    str_fl = float(str_bef)

    # Digits after decimal point
    num_dec = fl_num - int(fl_num)
    num_dec = str(num_dec)
    num_dec = num_dec[0:aft_int_num + 2]

    return str_fl + float(num_dec) 


print(cropNumber(1234.5678, 2, 3))
