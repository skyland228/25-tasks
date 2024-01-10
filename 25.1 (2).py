def GoodNumber(number):
    div = 2
    divisors = []
    while div * div < number:
        if number % div == 0:
            divisors.append(div)
            divisors.append(number // div)
        div += 1
    if div * div == number:
        divisors.append(div)
    return divisors


ind = 0
for number in range(89000000000, 89010000000):

    if number ** 0.5 % 1 == 0 and 16 in GoodNumber(number):
        ind += 1
        print(number, ind)