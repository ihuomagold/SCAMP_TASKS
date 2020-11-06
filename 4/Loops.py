# USING THE FOR LOOP
# Example 1

# A simple Loop
print("I will display some numbers.")
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(number)

#

# Example 2
# Using the range function with the "for" loop

# A for loop that displays a following set of numbers:
for x in range(0, 1001, 10):
    print(x)

#

# Example 3
# Nested "for" loop

# This program simulates a digital clock

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)

#

# This program averages the number of test scores. It asks the user for the number
# of students and the number of test scores per student.

# Get the number of students
num_students = int(input("How many students do you have?: "))

# Get the number of test scores per student
num_of_test_scores = int(input("How many test scores per student?: "))

# Get the average test score per student

for student in range(num_students):
    # Initialize an accumulator for test scores
    total = 0.0
    # Get a student's test scores
    print("Student number", student + 1)
    print("----------------")
    for test_num in range(num_of_test_scores):
        print("Test number", test_num + 1, end="")
        score = float(input(": "))
        total += score
    # Calculate the average score for this student
    average = total / num_of_test_scores
    # Display the average test score.
    print("The average for student number", student + 1, "is:", average)
    print()

# USING THE WHILE LOOP
# Example 1

# A simple "while" loop
numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

while denominator == 0:
    print("Division is not possible.")
    denominator = int(input("Enter correct denominator: "))
dividend = numerator / denominator
print(dividend)
print()

#

# Example 2:
# Program to calculate a series of sales commission

# Create a variable to control the loop
keep_going = "y"

# calculate a series of commissions
while keep_going == "y":
    # get a salesperson's sales and commission rate
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate:  "))

    # calculate the commission
    commission = sales * comm_rate

    # display the commission

    print("The commission is $", format(commission, ",.2f"), sep="")

    # ask if the user wants to do another one

    keep_going = input("Do you want to calculate another " + \
                       "commission (Enter y for yes): ")
