import random
result = []
numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(numbers)
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i+j) == 0:
            result.append(i)
            result.append(j)
print('Указанное число: ', n)
print('Пароль: ', *result)





