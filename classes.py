class Budget:

    def __init__(self, category):
        self.category = category
        self.amount = 5000

    def deposit(self, amount):
        self.amount += amount
        return self.amount
    
    def check_balance(self, amount):
        if self.amount < amount:
            return False
        else:
            return True    

    def withdraw(self, amount):
        self.amount -= amount
        return self.amount

    def transfer(self, amount, category):
        if self.check_balance(amount) == True:
            self.amount -= amount
            category.amount += amount
            return "You have transferred () to ()".format(amount, category.category)
        else:
            return "You do not have enough balance to perform this transfer"

        pass

category = Budget("Clothing")
print("This is a deposit for clothing", category.deposit(10000))
print("This is a withdrawal for clothing", category.withdraw(8000))

category_1 = Budget ("Food")
print("This is a deposit for food", category_1.deposit(20000))

category_2 = Budget("Entertainment")
print(category_2.transfer(6000, "Entertainment"))



#category_2 = Budget ("Entertainment")