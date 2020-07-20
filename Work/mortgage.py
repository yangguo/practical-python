# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 1+12*5
extra_payment_end_month = 12*(5+4)
extra_payment = 1000

month = 0
exit = 0

while principal > 0 and exit ==0:
    month+=1
    if month >= extra_payment_start_month and month<=extra_payment_end_month:
        if principal * (1+rate/12) - payment - extra_payment>=0:
            principal = principal * (1+rate/12) - payment - extra_payment
            total_paid = total_paid + payment + extra_payment
        else: exit=1
    else:
        if principal * (1+rate/12) - payment>=0:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment
        else: exit=1
    if exit==0:
        # print(month,round(total_paid,2),round(principal,2))
        fstr = f'month{month} total paid ${total_paid:0.2f},principal is ${principal:0.2f}'
        print(fstr)
    else:
        month-=1
    
print('Total paid', f'${total_paid:0.2f}')
print('Total month', month)
