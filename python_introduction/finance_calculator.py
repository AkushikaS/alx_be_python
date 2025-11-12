n = int(input("Enter your monthly income:"))
print(n)
m = int(input("Enter your total monthly expenses:"))
print(m)

Monthly_Savings = n - m
print(f"Your monthly savings are {Monthly_Savings}")

Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print(f"Projected savings after one year, with interest is: {Projected_Savings}")
