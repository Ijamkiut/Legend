downpayment = int(input("Please Enter Your DownPayment : "))

afterdownpayment = 90000-downpayment

if downpayment <= 9000:
    print("You Are Not Eligible For The Bank Loan")
else:
    year = int(input("How Long You Want Make a Loan in Year(1 to 9 years only) : "))

    total = 0.027 * afterdownpayment * year
    montly =(afterdownpayment + total)/(year*12)
    print("You Need To Pay RM ",round(montly,2),"montly as your monthly payment")

