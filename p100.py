class Atm:
    def __init__(self,cardnumber,atmpin):
        self.cardnumber=cardnumber
        self.pin=pin


    def balance(self):
        print("Your balance is 100000")

    def withdrawcash(self,amount):
        balanceamount=100000-amount
        print("your current balance is : ",str(balanceamount))  

def main():
    cd= input("enter your card number :- ")
    pin=input("enter your atm pin number :- ")

    person=Atm(cd,pin)
    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity=int(input("enter the task number : "))

    if (activity == 1):
        person.balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        person.withdrawcash(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()