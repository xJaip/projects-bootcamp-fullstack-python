import random
numbers =[]
for i in range(3):
    numbers.append(random.random())

numbers.sort(reverse=True)
print(numbers)
    