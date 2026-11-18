print("---Salary calculator---".title())
name= input("What is your name? ")
monthly_salary= int(input("How much do you make monthly? "))
if monthly_salary >= 300000:
  tax = 0.15
elif monthly_salary >= 100000:
  tax= 0.10
else:
  tax = 0.05
tax_ded= monthly_salary * tax
take_home= monthly_salary-tax_ded
print(name)
print(f"${monthly_salary:,}")
print(f"{tax * 100:.0f}%")
print(f"${tax_ded:,.0f}")
print(f"${take_home:,.0f}")



  
