def DIV(number):
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
def simple_number(div):
    d = 2
    while d * d <= div:
        if div % d == 0:
            return False
        d += 1
    return True

for number in range(2436700,2570609):
    divisors = DIV(number)
    if len(divisors) > 0 and simple_number(divisors[0]) :
        if divisors[0] != 2 and divisors[0] == len(divisors):
            print(number,divisors[0])