
'''
Define a Transaction class, in which each instance represents either a deposit
or a withdrawal from a bank account. When creating a new instance of Transaction,
you’ll need to specify an amount—positive for a deposit and negative for a withdrawal.
Use a class attribute to keep track of the current balance, which should be equal
to the sum of the amounts in all instances created to date.
'''

class Transaction:
    balance = 0

    def __init__(self, amount):
        self.amount = amount
        Transaction.balance += amount

    def __repr__(self):
        return str(Transaction.balance)
        
        

t = Transaction(70)
t = Transaction(-20)

print(t)  # Returns 50
