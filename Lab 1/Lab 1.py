# Kyle Johnson
# ETEC3702 – Concurrency 5:00 PM
# Paul Yost
# 1-24-21
# Lab 1 – Simple Threads in Python

# Part 1
import time
import random
import threading

class BankAccount(object):
    def __init__(self,initialBalance):
        self.balance=initialBalance
        self.transactionLog=[]
        self.transactionLog.append("initial balance:" + str(initialBalance))
    def getBalance(self):
        time.sleep(random.uniform(0,0.00001))
        temp=self.balance
        time.sleep(random.uniform(0,0.00001))
        self.transactionLog.append("getBalance:"+str(temp))
        return temp
    def setBalance(self,amount):
        time.sleep(random.uniform(0,0.00001))
        self.balance=amount
        time.sleep(random.uniform(0,0.00001))
        self.transactionLog.append("setBalance:"+str(amount))
    def withdraw(self,amount):
        withBalance = self.getBalance() - amount
        self.setBalance(withBalance)
        self.transactionLog.append("widthdraw("+str(amount)+")")
    def deposit(self,amount):
        depBalance = self.getBalance() + amount
        self.setBalance(depBalance)
        self.transactionLog.append("deposit("+str(amount)+")")

myAccount = BankAccount(
    initialBalance = 1000
    )

# myAccount.deposit(500)
# myAccount.withdraw(50)
# myAccount.withdraw(10)
# print(myAccount.transactionLog)
# print("Final Balance: " + str(myAccount.balance))

# Part 2
# a
# Assuming that all three method's were executed concurrently there would be 20 orderings.
# b
# There is 7 different possibilities for Final balances 
# 1500, 1490, 1450, 1440, 940, 950, 990

# Part 3
# a
for i in range(30):
    myAccount = BankAccount(
        initialBalance = 1000
    )
    t1 = threading.Thread(target=myAccount.deposit(500,))
    t2 = threading.Thread(target=myAccount.withdraw(50,))
    t3 = threading.Thread(target=myAccount.withdraw(10,))
    t1.start()
    t2.start()
    t3.start()
    # print("Threads are now running in Part 3")
    t1.join()
    t2.join()
    t3.join()
    # print("Threads done.")
    print(myAccount.transactionLog)
    print("Final Balance: " + str(myAccount.balance))
# b
# The output produced the result of 1440 everytime which is what was desired from the analysis of part 2,
# and is one of the expected values. This implementation is not perfect though and can result in incorrect values
# as shown in part 2.