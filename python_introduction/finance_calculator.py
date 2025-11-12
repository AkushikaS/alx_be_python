monthly_income = int(input("Enter your monthly income:"))
print(monthly_income)
monthly_expenses = int(input("Enter your total monthly expenses:"))
print(monthly_expenses)

monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are {monthly_savings}")

Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest is: {Projected_Savings}")
