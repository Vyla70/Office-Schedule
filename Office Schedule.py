import pandas as pd
import numpy as np

# TASK 1

# Assigning day numbers to days of the week
Monday = []
for i in range(1, 366, 7):
    Monday.append(i)

Tuesday = []
for i in range(2, 366, 7):
    Tuesday.append(i)

Wednesday = []
for i in range(3, 366, 7):
    Wednesday.append(i)

Thursday = []
for i in range(4, 366, 7):
    Thursday.append(i)

Friday = []
for i in range(5, 366, 7):
    Friday.append(i)

workingday_num = Monday + Tuesday + Wednesday + Thursday + Friday
workingday_num.sort()

# Create an ordered list of working day names
day_name = []
for i in workingday_num:
    if i in Monday:
        day_name.append("Monday")
    elif i in Tuesday:
        day_name.append("Tuesday")
    elif i in Wednesday:
        day_name.append("Wednesday")
    elif i in Thursday:
        day_name.append("Thursday")
    else:
        day_name.append("Friday")

# Getting the Fibonacci sequence as a list
Fibonacci = [1, 2]
i1 = 0
i2 = 1
while Fibonacci[-1] < workingday_num[-1]:
    i3 = Fibonacci[i1] + Fibonacci[i2]
    Fibonacci.append(i3)
    i1 += 1
    i2 += 1
Fibonacci.remove(Fibonacci[-1])

# Getting a list of Prime numbers
Prime = []
for num in range(1, 366):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            Prime.append(num)

# Assigning 'in office' workdays to employee names
Anna = Monday + Tuesday + Friday[0::2]
Barbara = Tuesday + Wednesday + Thursday
Charlie = Fibonacci + Prime

# Get a binary schedule of office/home days (1 = office, 0 =home)
Anna_days = []
for i in workingday_num:
    if i in Anna:
        Anna_days.append(1)
    else:
        Anna_days.append(0)

Barbara_days = []
for i in workingday_num:
    if i in Barbara:
        Barbara_days.append(1)
    else:
        Barbara_days.append(0)

Charlie_days = []
for i in workingday_num:
    if i in Charlie:
        Charlie_days.append(1)
    else:
        Charlie_days.append(0)

# Create Pandas dataframe
data = {"Day_num": workingday_num,
        "Day_name": day_name,
        "Anna": Anna_days,
        "Barbara": Barbara_days,
        "Charlie": Charlie_days
        }
df = pd.DataFrame(data)

# Adding office utilization % column to check if policy is violated
Employee_list = ["Anna", "Barbara", "Charlie"]
df["Office utilization"] = df[Employee_list].sum(axis=1) / len(Employee_list)
df["Policy violated"] = df["Office utilization"] > (2 / 3)
Problem_days = df.loc[df["Policy violated"] == True]

# Display working schedule & dataframe of days
print("Working schedule:")
print(df)

# Display problematic days, where policy is violated
print("Problematic days, where policy is violated:")
print(Problem_days)


# TASK 2

# Calculate number of office days for new employees based on 20% chance
# Convert list to Numpy array to use built-in random function to assign office days
officedays = int(len(workingday_num) * 0.2)  # = 52
workingday_array = np.array(workingday_num)

# Get input and create a list of employee names
userinput = input("Enter a list of employees to be added, separated by comma:")
input_list = userinput.split(",")

# Define function to add new employees to the schedule
def add_employee(lst):
    loc = 5 # Column number to insert first employee to (to keep input order)

    for x in lst:

        # Assign the 52 random office days to employee and order it by day numbers
        Employee = list(np.random.choice(workingday_array,officedays,None))
        Employee.sort()

        # Create binary schedule for new employee
        Employee_days = []
        for i in workingday_num:
            if i in Employee:
                Employee_days.append(1)
            else:
                Employee_days.append(0)

        # Insert new employee's schedule to the dataframe (while keeping input order)
        df.insert(loc,x,Employee_days)
        loc += 1

        # Add new employee to the list of all employees
        Employee_list.append(x)

# Run defined function
add_employee(input_list)

# Updating office utilization column to include newly inserted employee columns
df["Office utilization"] = df[Employee_list].sum(axis=1) / len(Employee_list)
df["Policy violated"] = df["Office utilization"] > (2 / 3)
Problem_days = df.loc[df["Policy violated"] == True]

# Display updated schedule
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)

# Display problematic days, where policy is violated
print("")
print("On the following days the maximum attendance rule is violated:")
print("")
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(Problem_days)