def remaining_balance(principal, annual_interest_rate, duration, num_pays):
    n = duration*12
    r = (annual_interest_rate/100)/12
    remaining_loan = 0

    if r == 0:
        remaining_loan = principal*(1-(num_pays/n))
    else:
        remaining_loan = principal*(((1+r)**n)-((1+r)**num_pays))/((1+r)**n-1)

    return remaining_loan
    

print(remaining_balance(1000.00, 4.5, 5, 12))

