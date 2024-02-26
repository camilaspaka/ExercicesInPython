def euclidean_division(x,y):
    quotient = x // y
    remainder = x % y
    print(f"{quotient} remainder {remainder}")

euclidean_division(10, 3)
euclidean_division(11, 3)
0

#divmod

euclidean_divisionn = divmod(5, 2)
print(euclidean_divisionn)

#another way

exercicio = quotient, remainder = divmod(5, 2)
print(exercicio)