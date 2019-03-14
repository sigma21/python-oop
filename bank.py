# class bank
#
#     .methods
#     add customer
#     list customers   in a dictionary with Id and name as key value pair
#     remove customer
# Bank(customer)
# deposit
# withdraw
# display balance
# show transactions  in a dictionary with time stamp and type of action and amount
# gui/database/pin safety

import random
import time
t = time.localtime()


class BankAccount:

    def __init__(self):
        self.customers = {}
        self.deposit = {}
        self.withdrawal = {}

    def initializeAccount(self, customerName, initialAmount=0):
        self.customerID = random.randint(1, 100)
        self.customerName = customerName
        self.currentBalance = initialAmount
        self.customers[self.customerID] = self.customerName

    def listCustomers(self):
        print(self.customers)

    def displayCustomerInfo(self): ##???##
        print("""\n\t\tCustomer Info
        Name: {}
        Bank ID: {}
        Current Balance: {}
        """.format(self.customerName, self.customerID, self.currentBalance))

    def removeCustomer(self):
        pass

    def depositMoney(self, depositAmount):
        self.currentBalance += depositAmount
        print(depositAmount, " added to your balance.\nCurrent balance: ", self.currentBalance)
        self.deposit[time.asctime(t), " Deposit"] = depositAmount

    def withdrawMoney(self, withdrawalAmount):
        if self.currentBalance >= withdrawalAmount:
            self.currentBalance -= withdrawalAmount
            print(withdrawalAmount, " deducted from your balance.\nCurrent balance: ", self.currentBalance)
            self.withdrawal[time.asctime(t), " Withdrawal"] = withdrawalAmount
        else:
            print("Sorry! Insufficient funds.")

    def displayBalance(self):
        print("""Name: {}
        Current Balance: {}
        """.format(self.customerName, self.currentBalance))

    def showTransactions(self):
        #should order it according to transaction time
        print(self.deposit, self.withdrawal)

################################################


# new_account = BankAccount()
#
# new_account.addCustomer("Alex Felix")
# new_account.addCustomer("Mike Murphy", 500)
# new_account.listCustomers()
#account.felix.addmoneyy?????



alex=BankAccount()
alex.initializeAccount("Alexander Felix", 500)
print("*"*20)
alex.listCustomers()
print("*"*20)
alex.displayCustomerInfo()
print("*"*20)
alex.depositMoney(100)
print("*"*20)
alex.withdrawMoney(250)
print("*"*20)
alex.displayBalance()
print("*"*20)
alex.showTransactions()




