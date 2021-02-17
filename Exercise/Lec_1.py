class Account:
    accountCount = 0
    total = 0

    def __init__(self, name, accountNo):
        self.name = name
        self.accountNo = accountNo
        self.balance = 0
        Account.accountCount +=1
        print("Account " + self.accountNo + " created.")
        print("Account count = " + Account.accountCount.__str__())
    
    def withdraw(self, amount):
        self.amount = amount
        Account.total -= amount
        print("Withdraw Successful! Balance = " + Account.total.__str__())
   
    def deposit(self,amount):
       self.amount = amount
       Account.total += amount
       print("Deposit Successful! Balance = " + Account.total.__str__())

    def printAccountInfo(self):
        print(self.accountNo + " " + self.name)
    

testAcc = Account("Haikal", "Operator")
testAcc.deposit(1000)
testAcc.withdraw(100)
testAcc.deposit(50)