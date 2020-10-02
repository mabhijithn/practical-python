# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
originial_payment = 2684.11
total_paid = 0.0
count = 1
extra_payment_start_month = 61
extra_payment_end_month = extra_payment_start_month+(4*12)-1
extra_payment = 1000

while principal > 0:
    if(count>=extra_payment_start_month and count<=extra_payment_end_month):
        payment = originial_payment + extra_payment
    else:
        payment = originial_payment
    principal = principal * (1+rate/12) - payment
    if principal<0:
        payment = payment + principal
        principal = 0
    total_paid = total_paid + payment
    s = f'{count:3d} {total_paid:6.2f} {principal:6.2f}'
    print(s)
    #print(count,total_paid,round(principal))
    count = count+1    
s = f'Months:{count} Total Paid:{total_paid:6.2f}'
print(s)