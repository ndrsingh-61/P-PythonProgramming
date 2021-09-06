print("Welcome to the tip calculator ")
total_bill = float(input("what was the total bill? $"))
no_of_people = float(input("how many people to split the bill? "))
tip_percent = float(input("what percentage tip would you like to give? 10, 12, or 15? "))
ind_pay = (total_bill + ((tip_percent/100) * total_bill))/5
print("Each person should pay: $", round(ind_pay, 1))