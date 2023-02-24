import pandas as pd
import numpy as np

Loan_amount=int(input('Please enter the loan amount: '))# enter loan amount
Tenor=int(input("Please enter the tenor: ")) # enter the tenor of the loan
Interest=float(input("please enter rate of Interest: ")) # enter the rate of interest

# convert the rate of interest into yearly basis
monthly_rate=(Interest/100)/12 

# calculate the monthly EMI amount
monthly_payment=(monthly_rate*Loan_amount)/(1-(1 + monthly_rate)**(-Tenor))
repayment_schedule=[]
balance=Loan_amount
for i in range(Tenor):
    interest=monthly_rate*balance
    principal_paid=monthly_payment - interest
    balance -= principal_paid
    repayment_schedule.append((i+1,balance,principal_paid,interest,monthly_payment)) 
                              
print("Payment\tBalance\tPrincipal\tInterest\tPayment")
for i,(month,balance,principal_paid,interest,monthly_payment)in enumerate (repayment_schedule):
    print(f"{month}\t{balance:.2f}\t{principal_paid:.2f}\t{interest:.2f}\t{monthly_payment:.2f}")   
