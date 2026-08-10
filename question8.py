employee = ("Arjun", "Developer", 45000, 3)
name, designation, salary, experience = employee
annual_salary = salary * 12
if experience < 2:
    bonus = annual_salary * 5 / 100
elif experience <= 5:
    bonus = annual_salary * 10 / 100
else:
    bonus = annual_salary * 15 / 100
total = annual_salary + bonus

print("Employee Name:", name)
print("Designation:", designation)
print("Experience:", experience, "years")
print("Monthly Salary:", salary)
print("Annual Salary:", annual_salary)
print("Bonus:", bonus)
print("Total Annual Compensation:", total)
