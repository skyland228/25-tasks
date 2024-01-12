from math import ceil
f = open('27_1B.txt')
n = int(f.readline())
elems = []
sum = 0
rightSum = 0
leftSum = 0
for i in range(0, n):
    a, b = map(int, f.readline().split())
    elems.append([a, ceil(b / 36)])
elems.sort() # в файле в первой строке почему-то было большое число, хотя вроде бы числа должны идти по возрастанию
cost = [0] * n
for i in range(1, n):
    cost[0] += (elems[i][0] - elems[0][0]) * elems[i][1]
    rightSum += elems[i][1]
for i in range(1, n):
    leftSum += elems[i - 1][1]
    cost[i] = cost[i - 1] - rightSum * (elems[i][0] - elems[i - 1][0]) + leftSum * (elems[i][0] - elems[i - 1][0])
    rightSum -= elems[i][1]
print(min(cost))