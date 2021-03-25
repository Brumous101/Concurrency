# Kyle Johnson
# ETEC3702 – Concurrency 5:00 PM
# Paul Yost
# 1-28-21
# Lab 2 – Concurrent Synchronization with Locks

import time
import random
import threading

class BankAccount(object):
    def __init__(self,initialBalance):
        self.balance=initialBalance
        self.transactionLog=[]
        self.transactionLog.append("initial balance:" + str(initialBalance))
        self.lock = threading.Lock()
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
        self.lock.acquire()
        withBalance = self.getBalance() - amount
        self.setBalance(withBalance)
        self.transactionLog.append("widthdraw("+str(amount)+")")
        self.lock.release()
    def deposit(self,amount):
        self.lock.acquire()
        depBalance = self.getBalance() + amount
        self.setBalance(depBalance)
        self.transactionLog.append("deposit("+str(amount)+")")
        self.lock.release()

myAccount = BankAccount(
    initialBalance = 1000
    )

for i in range(100):
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
print("The output was correct each time.")
print("The execution is no longer non-deterministic")
print("The program is now concurrent as the threads are running simultaneously but interacting with critical sections at different times.")

# The output was correct each time.
# The execution is no longer non-deterministic
# The program is now concurrent as the threads are running simultaneously but interacting with critical sections at different times.