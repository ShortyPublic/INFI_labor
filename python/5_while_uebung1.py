from random import randrange
sum = 0
while True:
    num = randrange(10, 30)
    if num == 25 or num == 15:
       break
    sum += num
print(sum) 