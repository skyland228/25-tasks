def havesix(div):
    while div > 0:
        if div % 1000 == 666:
            return 1
        div //= 10
    return 0
def damn_sums(fee):
    div = 2
    divisors = []
    while div * div < fee:
        if fee % div == 0:
            divisors.append(div)
            divisors.append(fee //div)
        div += 1
    if div * div == fee:
        divisors.append(div)
    return divisors
for fee in range(1000000,1100000):
    divisors = damn_sums(fee)
    kdiv = 0
    for i in range(len(divisors)):
        kdiv += havesix(divisors[i])
    if kdiv == 4:
        print(divisors)
        print(fee, int(fee * 0.4))
