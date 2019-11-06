# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:15:18 2019

@author: David
"""

portion_down_payment = .25
current_savings = 0
r = .04
count = 0
total_cost = 130000
semi_annual_raise = .07
error = 100
number_of_months = 36
months_to_save = 0
high = 10000
low = 0
guess = (high + low)/2
down_payment = total_cost*portion_down_payment

annual_salary = int(input("Enter your annual salary: "))


while abs(current_savings - down_payment) >= error and count < 13:
    portion_saved = guess/10000
    monthly_salary = annual_salary/12
    months_to_save = 0
    current_savings = 0
    
    while current_savings < down_payment:
        if(months_to_save % 6 == 0 and months_to_save != 0):
            monthly_salary +=  monthly_salary*semi_annual_raise
        current_savings += monthly_salary * portion_saved + (current_savings * (r/12))
        months_to_save += 1
        
    if months_to_save > number_of_months:
        low = guess
    else:
        high = guess
        
    guess = (high + low)/2
    count += 1
       
if count < 13:
    portion_saved = guess/10000
    print("Best savings rate: " + str(portion_saved))
    print("Steps in Bisection search: " + str(count))
else:  
    print("It is not possible to pay the down payment in three years.")      
    