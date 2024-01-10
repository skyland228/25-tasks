ind = 1
for number in range(89000000000,89010000000):
    if number ** 0.5 % 1 == 0 and number % 16 == 0:
        print(number, ind)
        ind += 1