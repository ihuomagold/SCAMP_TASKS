#  Example 1
# Using the if-else statement

# Age Classifier:
# This program asks the user to enter a person’s age.
# The program displays a message indicating whether the person is
# an infant, a child, a teenager, or an adult.
# Following are the guidelines:
# • If the person is 1 year old or less, he or she is an infant.
# • If the person is older than 1 year, but younger than 13 years, he or she
# is a child.
# • If the person is at least 13 years old, but less than 20 years old,
# he or she is a teenager.
# • If the person is at least 20 years old, he or she is an adult.

# Get the users age
User_age = int(input("Enter your age: "))

# Determine the age threshold
if User_age <= 1:
    print("You are an infant.")
else:
    if User_age > 1 and User_age < 13:
        print("You are a child.")
    else:
        if User_age >= 13 and User_age < 20:
            print("You are a teenager.")
        else:
            print("You are an adult.")

#

# Example 2
# Using the if-elif-else statement

# Areas of Rectangles:
# The area of a rectangle is the rectangle’s length times its width.
# This program asks for the length and width of two rectangles.
# The program tells the user which rectangle has the greater area,
# or if the areas are the same.

L_A = int(input("Enter the length of rectangle A: "))
W_A = int(input("Enter the width of rectangle A: "))

L_B = int(input("Enter the length of rectangle B: "))
W_B = int(input("Enter the width of rectangle B: "))

Area_of_A = (L_A * W_A)
Area_of_B = (L_B * W_B)

if Area_of_A > Area_of_B:
    print("The area of rectangle A is greater than the area of rectangle B.")
elif Area_of_B > Area_of_A:
    print("The area of rectangle B is greater than the area of rectangle A.")
else:
    print("The areas of both rectangles are the same.")

#

# Example 3

# Day of the Week:
# This program asks the user for a number in the range of 1 through 7.
# The program displays the corresponding day of the week, where 1 = Monday, 2 = Tuesday,
# 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.
# The program displays an error message if the user enters a number that is outside
# the range of 1 through 7.

day_1 = "Monday"
day_2 = "Tuesday"
day_3 = "Wednesday"
day_4 = "Thursday"
day_5 = "Friday"
day_6 = "Saturday"
day_7 = "Sunday"

Day_of_the_week = int(input("Enter a number in the range of 1 to 7: "))

if Day_of_the_week == 1:
    print(day_1)
elif Day_of_the_week == 2:
    print(day_2)
elif Day_of_the_week == 3:
    print(day_3)
elif Day_of_the_week == 4:
    print(day_4)
elif Day_of_the_week == 5:
    print(day_5)
elif Day_of_the_week == 6:
    print(day_6)
elif Day_of_the_week == 7:
    print(day_7)
else:
    print("Error!")
