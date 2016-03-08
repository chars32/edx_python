def loan_payments(principal, annual_interest_rate, duration):
    n = duration*12
    r = (annual_interest_rate/100)/12
    monthly_payment = 0

    if r == 0:
        monthly_payment = principal/n
    else:
        monthly_payment = principal*((r*(1+r)**n)/((1+r)**n-1))

    return monthly_payment

print(loan_payments(1000.00, 4.5, 5))
