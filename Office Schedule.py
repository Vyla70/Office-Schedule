import pandas as pd
import numpy as np

# ---TASK 1---

# Assign day numbers to days of the week
Monday = [i for i in range(1, 366, 7)]
Tuesday = [i for i in range(2, 366, 7)]
Wednesday = [i for i in range(3, 366, 7)]
Thursday = [i for i in range(4, 366, 7)]
Friday = [i for i in range(5, 366, 7)]

# Create a comprehensive list of all working day numbers
workingday_num = Monday + Tuesday + Wednesday + Thursday + Friday
workingday_num.sort()

# Create an ordered list of working day names (to be shown next to working day numbers)
day_name = ["Monday" if i in Monday
            else "Tuesday" if i in Tuesday
            else "Wednesday" if i in Wednesday
            else "Thursday" if i in Thursday
            else "Friday" for i in workingday_num]

# Getting the Fibonacci sequence as a list
Fibonacci = [1, 2]
while Fibonacci[-1] < workingday_num[-1]:
    var = Fibonacci[-2] + Fibonacci[-1]
    Fibonacci.append(var)
Fibonacci.remove(Fibonacci[-1])

# Getting a list of Prime numbers
prime = [x for x in range(2, 366) if all(x % y != 0 for y in range(2, x))]

# Assigning 'in office' workdays to employee names
Anna = Monday + Tuesday + Friday[1::2]
Barbara = Tuesday + Wednesday + Thursday
Charlie = Fibonacci + prime

# Get a schedule of office/home days in a binary format (1 = office, 0 =home)
Anna_days = [1 if i in Anna else 0 for i in workingday_num]
Barbara_days = [1 if i in Barbara else 0 for i in workingday_num]
Charlie_days = [1 if i in Charlie else 0 for i in workingday_num]

# Create Pandas dataframe
data = {
    "Day_num": workingday_num,
    "Day_name": day_name,
    "Anna": Anna_days,
    "Barbara": Barbara_days,
    "Charlie": Charlie_days
        }
df = pd.DataFrame(data)

# Adding office utilization column (as %) to check if policy is violated
employee_list = ["Anna", "Barbara", "Charlie"]
df["Office utilization"] = df[employee_list].sum(axis=1) / len(employee_list)
df["Policy violated"] = df["Office utilization"] > (2 / 3)
problem_days = df.loc[df["Policy violated"] == True]

# Display problematic days, where policy is violated
print("TASK 1 output")
print('\n')
print("Problematic days, where policy is violated:")
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(problem_days)

# ---TASK 2---

# Calculate number of office days for new employees based on 20% chance annually
office_days = int(len(workingday_num) * 0.2)  # = 52

# Convert list to Numpy array to assign random office days in the function
workingday_array = np.array(workingday_num)


# Define function to add new employees to the schedule
def add_employee(lst):

    loc = len(employee_list) + 2  # Column number to insert first employee to (to keep input order)

    for x in lst:

        # Assign the 52 random office days to employee and order it by day numbers
        employee = list(np.random.choice(workingday_array, office_days, None))
        employee.sort()

        # Create schedule for new employee in a binary format
        employee_days = [1 if i in employee else 0 for i in workingday_num]

        # Insert new employee's schedule to the dataframe (while keeping input order)
        df.insert(loc, x.strip(" "), employee_days)
        loc += 1

        # Add new employee to the list of all employees
        employee_list.append(x.strip(" "))

# Run function to add 3 predefined employees
my_input = ["David", "Emily", "Frank"]
add_employee(my_input)

# Updating office utilization column to include newly inserted employee columns
df["Office utilization"] = df[employee_list].sum(axis=1) / len(employee_list)
df["Policy violated"] = df["Office utilization"] > (2 / 3)
problem_days = df.loc[df["Policy violated"] == True]

# Display problematic days, where policy is violated
print('\n')
print("TASK 2 output")
print('\n')
print("On the following days the maximum attendance rule is violated:")
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(problem_days)

# ---TASK2 (User Input)---

# Get user input and create a list of employee names from it + run function
print('\n')
userinput = input("Enter a list of employees to be added, separated by comma:")
input_list = userinput.split(",")
add_employee(input_list)

# Updating office utilization column to include newly inserted employee columns
df["Office utilization"] = df[employee_list].sum(axis=1) / len(employee_list)
df["Policy violated"] = df["Office utilization"] > (2 / 3)
problem_days = df.loc[df["Policy violated"] == True]

# Display updated schedule
print("Full schedule after all update:")
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)

# Display problematic days, where policy is violated
print('\n')
print("On the following days the maximum attendance rule is violated:")
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(problem_days)
