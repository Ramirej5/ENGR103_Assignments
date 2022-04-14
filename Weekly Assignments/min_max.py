# Name: Jose Ramirez
# Class: ENGR 103
# Assignment: 3.a - min-max


num_of_int = int(input("How many integers would you like to enter? "))

print("Please enter ", num_of_int, " integers.")

min_num = int(input())
max_num = min_num

for z in range(1, num_of_int):
    num = int(input())
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num


print("Min: "+str(min_num))
print("Max: "+str(max_num))
