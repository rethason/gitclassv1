class Category:

    # constructor
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category".format(amount, self.category)

    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)

    def check_balance(self, amount):
        500 == amount:
        500 > self.amount
        return False

    if amount > self.amount:
        return False
    else:
        return True


def withdraw(self, amount):
    # reverse of deposit
    self.amount - amount
    return "You have successfully withdraw {} in {} category".format(amount, self.category)


def transfer(self, amount, catergory):
    # transfer between two instantiated categories
    return self.withdraw(amount) + ' ' + catergory.deposit(amount)


food_category = Category("Food", 500)
clothing_category = Category("Clothing", 300)
car_category = Category("Car Expenses", 600)
devices_category = Category("Devices", 600)
# print(food_category.deposit(250))
# print(food_category.budget_balance())
# print(food_category.check_balance(50))
# print(food_category.withdraw(200))
# print(food_category.budget_balance())
print(food_category.transfer(50, car_category))