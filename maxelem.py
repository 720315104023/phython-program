a = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number '))
    a.append(numbers)

print("Maximum element in the list is :", max(a))
