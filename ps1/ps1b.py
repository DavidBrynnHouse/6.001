# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:05:59 2019

@author: David
"""

portion_down_payment = .25
current_savings = 0
r = .04
months_to_save = 0

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home:​ "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

down_payment = total_cost*portion_down_payment
monthly_salary = annual_salary/12

while current_savings < down_payment:
    if(months_to_save % 6 == 0 and months_to_save != 0):
        monthly_salary +=  monthly_salary*semi_annual_raise
    current_savings += monthly_salary * portion_saved + (current_savings * (r/12))
    months_to_save += 1

print("Number of Months: " + str(months_to_save))