import random

symvols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

count = int(input("Введите длину пароля"))

result = "8"

for i in range(count):
    result += random.choice(symvols)

print(result)
