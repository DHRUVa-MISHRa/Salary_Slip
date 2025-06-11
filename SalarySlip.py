n= input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
basic_salary = float(input("Enter Basic Salary: "))
hra = basic_salary * 0.20   
da = basic_salary * 0.10    
pf = basic_salary * 0.12    
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf
print("\n------ SALARY SLIP ------")
print("Employee Name :", n)
print("Employee ID   :", emp_id)
print("Basic Salary  : ₹", basic_salary)
print("HRA (20%)     : ₹", hra)
print("DA (10%)      : ₹", da)
print("PF (12%)      : ₹", pf)
print("---------------------------")
print("Gross Salary  : ₹", gross_salary)
print("Net Salary    : ₹", net_salary)
print("---------------------------")
