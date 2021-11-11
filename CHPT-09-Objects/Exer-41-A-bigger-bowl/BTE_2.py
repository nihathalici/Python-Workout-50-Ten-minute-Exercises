'''
Create a Phone class that represents a mobile phone. (Are there still nonmobile phones?)
The phone should implement a dial method that dials a phone number (or simulates doing so).
Implement a SmartPhone subclass that uses the Phone.dial method but implements its own
run_app method. Now implement an iPhone subclass that implements not only a run_app method,
but also its own dial method, which invokes the parent’s dial method but whose output is
all in lowercase as a sign of its coolness.
'''

class Phone():
    def __init__(self):
        pass

    def dial(self, number):
        return f'Dialing {number}'
        
        

class SmartPhone(Phone):
    def run_app(self, app_name):
        return f'Running an app: {app_name}'
    

class iPhone(SmartPhone):
    def run_app(self, app_name):
        return super().run_app(app_name).lower()


ph = Phone()
print(ph.dial(345))

ph2 = SmartPhone()
print(ph2.run_app('MyCall'))

ph3 = iPhone()
print(ph3.run_app('MyCall For IOS'))
