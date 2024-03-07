#Create Account class with 2 attributes - balance & account no.
#Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self , acc,bal): 
        self.balance = bal
        self.account_no = acc

    #debit metthod
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"was Debited")
        print("total balance = ",self.get_balance())
    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"was Credited")
        print("Total Balance = ",self.get_balance())

    def get_balance(self):
        return self.balance
    

acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
# print("\nAccount No :",acc1.account_no,"\nBalance = ",acc1.get_balance(),"\n")
