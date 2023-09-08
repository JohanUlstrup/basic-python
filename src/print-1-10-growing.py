
# Print the numbers described in the exercise
x =[]
""" for number in range(1,11):
    x.append(number)
    print(x) """

for number in range(1, 11):
    x.append(number)
    print(' '.join(map(str, x)))