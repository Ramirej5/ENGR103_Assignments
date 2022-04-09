# JOSE RAMIREZ
# ENGR 103
# ASSIGNMENT 2.C

coin_q = 0.25
coin_d = 0.10
Nickel = 0.05
Penny = 0.01

print("Please enter an amount in cents less than a dollar. ")

cent_input = float(input())

Q = int(cent_input // coin_q)
changeQ = int(cent_input) % coin_q

D = int(changeQ) // coin_d
changeD = int(changeQ) % coin_d


print("Your change will be: ")

print("Q: ", int(Q))
print("D: ", int(D))
print("N: ", int(N))
print("P: ", int(P))
