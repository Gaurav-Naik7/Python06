class BankAccount:

    ROI=10.5

    def __init__(self):
        self.Name=input("Enter Name: ")
        self.Amount=float(input("Enter Amount"))

    def Deposit(self):
        deposit=float(input("Enter Deposit amount"))
        self.Amount=self.Amount+deposit

    def Withdraw(self):
        withdraw=float(input("Enter withdrawal amount"))
        self.Amount=self.Amount-withdraw

    def CalculateIntrest(self):
        self.Amount=self.Amount+(BankAccount.ROI*self.Amount)/100

    def Display(self):
        print("Name is: ",self.Name)
        print("Amount is: ",self.Amount)

def main():
    obj1=BankAccount()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateIntrest()
    obj1.Display()

    obj2=BankAccount()
    obj2.Deposit()
    obj2.Withdraw()
    obj2.CalculateIntrest()
    obj2.Display()

if __name__=="__main__":
    main()
