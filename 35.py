class Customer:
    def __init__(self, customer_Id, customer_name, age, account):
        self.customer_Id = customer_Id
        self.customer_name = customer_name
        self.age = age
        self.account = account

    def withdraw(self, amount):
        print(amount, "Withdrawn")
        self.account.balance -= amount

    def take_card(self):
        pass

    def get_customer_Id(self):
        return self.customer_Id

    def get_customer_name(self):
        return self.customer_name

    def get_age(self):
        return self.age

    def get_account(self):
        return self.account


class Account:
    def __init__(self, account_type, balance, min_balance):
        self.account_type = account_type
        self.balance = balance
        self.min_balance = min_balance

    def get_account_type(self):
        return self.account_type

    def get_balance(self):
        return self.balance()

    def get_min_balance(self):
        return self.min_balance()

    def set_balance(self, left):
        self.balance = left


class PrivilegedCustomer(Customer):
    def __init__(self, bonus_points, customer_Id, customer_name, age, account):
        Customer.__init__(self, customer_Id, customer_name, age, account)
        self.bonus_points = bonus_points

    def get_bonus_points(self):
        return self.bonus_points

    def increase_bonus(self):
        if self.account.balance > 1000:
            self.bonus_points += 10
        else:
            self.bonus_points += 2


acc = Account("Savings", 1000, 500)
p = PrivilegedCustomer(100, 100, "Gopal", 43, acc)
am = int(input("Enter the amount you want to withdraw:"))
if (p.account.balance >= am):
    p.withdraw(am)
    if (p.account.balance < p.account.min_balance):
        print("LimitReachedException")
        print("Remove Card")
        print(p.account.balance)
    else:
        p.increase_bonus()
        print(p.get_bonus_points())
        print("Rest Balance", p.account.balance)
        print("Remove Card")
else:
    print("OverdrawException")