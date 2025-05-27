#prompt the user to enter their monthly income
monthly_income = int(input("Enter your monthly income: "))

monthly_expenses = int(input("Enter your monthly expenses: "))

#calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

#calculate the annual savings
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#display the annual savings
print(f"Your monthly savings are: {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {annual_savings}")