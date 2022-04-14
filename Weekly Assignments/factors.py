# Name: Jose Ramirez
# Class: ENGR 103
# Assignment: 3.b

# Write a program that asks the user to enter an integer,
# then prints a list of all positive integers that divide
# that number evenly, including itself and 1, in ascending order.

print("Please enter a positive integer: ")

number_entered = int(input())

print("The factors of",number_entered,"are:")

for n in range(1,number_entered):
    if number_entered%n==0:
        print(n)

print(number_entered)