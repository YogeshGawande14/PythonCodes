class Account:

    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance = self.balance - amount
        print("Rs.", amount, "debited")

    def credit(self, amount):
        self.balance = self.balance + amount
        print("Rs.", amount, "credited")

    def print_balance(self):
        print("Account No:", self.account_no)
        print("Balance:", self.balance)


# Create object
acc = Account(5000, 12345)

acc.debit(5000)
acc.credit(0)
acc.print_balance()