# Name: Jose Ramirez
# Class: ENGR 103
# Assignment: 3.a - min-max

print("How many integers would you like to enter? ")
num_of_int = int(input())

print("Please enter ", num_of_int, " integers.")

min_num = int(input())
max_num = min_num

for z in range(1, num_of_int):
    num_input = int(input())
    if num_input > max_num:
        max_num = num_input
    if num_input < min_num:
        min_num = num_input


print("Min: "+str(min_num))
print("Max: "+str(max_num))
