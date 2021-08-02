class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 100000")

    def withdrawl(self,amount):
        new_amount = 100000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    Card_number = int(input("Enter your card number: "))
    pin_number  = int(input("Enter your pin number: "))

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity: ")
    print("1.Balance Enquriy   2.withdrawl")
    print('Type 1 if you need to check your Balance Enquiry')
    print('Type 2 if you need to withdraw your cash')
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")

main()