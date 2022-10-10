from random import randrange
sum = 0
while True:
    num = randrange(20) + 10
    if num == 25 or num == 15:
       break
    sum += num
print(sum) 