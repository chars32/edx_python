# Your function for calculating payment goes here
def loan_payments(principal, annual_interest_rate, duration):
    n = duration*12
    r = (annual_interest_rate/100)/12
    monthly_payment = 0

    if r == 0:
        monthly_payment = principal/n
    else:
        monthly_payment = principal*((r*(1+r)**n)/((1+r)**n-1))

    return monthly_payment


# Your function for calculating remaining balance goes here
def remaining_balance(principal, annual_interest_rate, duration, num_pays):
    n = duration*12
    r = (annual_interest_rate/100)/12
    remaining_loan = 0

    if r == 0:
        remaining_loan = principal*(1-(num_pays/n))
    else:
        remaining_loan = principal*(((1+r)**n)-((1+r)**num_pays))/((1+r)**n-1)

    return remaining_loan

         
# Your main program goes here
principle=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))

monthly = int(loan_payments(principle, annual_interest_rate, duration))

resul = "LOAN AMOUNT:" ,principle "INTEREST RATE:"annual_interest_rate 
resul2= "DURATION (YEARS):" ,duration "MONTHLY PAYMENT:" ,monthly

print (resul,"\n",resul2)
