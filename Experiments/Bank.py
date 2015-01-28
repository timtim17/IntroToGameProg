from random import uniform as randfloat

class BankAccount:
    'A simple class to store money.'
    
    money = 0
    owner = ""

    def __init__(self, owner, money):
        self.owner = owner
        self.money = round(money, 2)

    def getOwner(self):
        return self.owner

    def getMoney(self):
        return self.money

    def deposit(self, amount):
        self.money = round(self.money + amount, 2)
        return True

    def withdraw(self, amount):
        if amount > self.money:
            print("Sorry, you do not have enough money to complete this transaction.")
            return False
        else:
            self.money -= amount
            return True
    
class ATM:
    'A simple class to distribute money.'

    def use(self, bankaccount):
        if not bankaccount.__class__.__name__ == "BankAccount":
            print("Not a BankAcount!")

        print("                               Welcome %s" % bankaccount.getOwner())

        choice = ""
        while not (choice == "1" or choice == "2" or choice == "3"):
            choice = raw_input('''
                            Choose an Option:
                            1: Get Amount of Money
                            2: Deposit Money
                            3: Withdraw

                            ''')

        if choice == "1":
            print("You have $%2.2f." % bankaccount.getMoney())
        else:
            while True:
                try:
                    amount = float(raw_input("How much money?     $"))
                    break;
                except ValueError:
                    print
                    
            if choice == "2":
                 bankaccount.deposit(amount)
            else:
                bankaccount.withdraw(amount)
                
            print("Done!")
                
        print("Have a nice day!")

account = BankAccount(raw_input("What is your name? => "), randfloat(0.00, 50.00))

while True:
    ATM().use(account)
