#Define a class to represent a bank account.
# Include the following details like name of the depositor, account number, type of account, balance amount in the account.
#Write methods to assign initial values, to deposit an amount, withdraw an amount after checking the balance, to display name, account number, account type and balance.
class Account:
    def getdata(self):
        self.name=input("Enter your name")
        self.acno=int(input("Enter the aacount number"))
        self.balance=0
        self.type=input("Enter the type of account")
    def deposite(self):
        d=int(input("enter the amount deposite"))
        self.balance=self.balance+d
    def withdraw(self):
        w=int(input("Enter the amount to withdraw"))
        if(self.balance>w):
            self.balance=self.balance-w
            print("New balance",self.balance)
        else:
            print("Insufficent balance")
    def display(self):
        print("Name",self.name)
        print("Account number",self.acno)
        print("Account type",self.type)
        print("Balance",self.balance)
obj1=Account()
obj1.getdata()
obj1.deposite()
obj1.withdraw()
obj1.display()

#Write the same prgrm with menu driven method
#1.Display account details
#2.Deposite
#3.Withdraw
#4.Balance enquiry
#5.Exit
print("Menu")
print("1.Display account details")
print("2.Deposite")
print("3.Withdraw")
print("4.Balance enquiry")
print("5.Exit")
p=int(input("Enter your choice"))
class Account:
    def getdata(self):
        self.name=input("Enter your name")
        self.acno=int(input("Enter the aacount number"))
        self.balance=0
        self.type=input("Enter the type of account")
    def deposite(self):
        d=int(input("enter the amount deposite"))
        self.balance=self.balance+d
    def withdraw(self):
        w=int(input("Enter the amount to withdraw"))
        if(self.balance>w):
            self.balance=self.balance-w
            print("New balance",self.balance)
        else:
            print("Insufficent balance")
    def display(self):
        print("Name",self.name)
        print("Account number",self.acno)
        print("Account type",self.type)
        print("Balance",self.balance)


#Write a Program to implement the following.
# Create a base class called Person consisting of name and code.
# Create 2 child classes a) Account with member_pay and b) Admin with experience and inherit the base class.
# Create a class Employee with name, code, experience and pay by inheriting the above classes.
class Person:
    def getdata(self):
        self.name=input("Enter the name")
        self.code=int(input("Enter the code"))
    def displaydata(self):
        print("Name",self.name)
        print("Code",self.code)
class Account(Person):
    def pay(self):
        self.pay=int(input("Enter the payment"))
    def displaypay(self):
        print("Salary",self.pay)
class Admin(Person):
    def experience(self):
        self.exp=input("Enter the experience")
    def displayexperience(self):
        print("Experience",self.exp)
class Employee(Account,Admin):
    pass   #If the last class had no stmts then use "pass"
emp1=Employee()
emp1.getdata()
emp1.pay()
emp1.experience()
emp1.displaydata()
emp1.displaypay()
emp1.displayexperience()