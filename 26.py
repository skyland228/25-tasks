f = open('26_2.txt')
k,n = map(int, f.readline().split())
a = [list(map(int,i.split())) for i in f]
a.sort()
count = 0
maxt = 0
klast = 0
for i in range(1,k+1): #ячейки нумеруются с одного видимо я про это забыл
    start = 0
    for x in a:
        if x[0] - start >= 1 and x[0] >= 0 and x[1] >= 0:
            count += 1
            start = x[1]
            if x[0] > maxt: # мы проверяем больше ли x[0] ячейки с последним временем сдачи багажа
                maxt = x[0]
                klast = i # и если да, то помещяем эту ячейку в переменную для последней ячейки
            x[0] = -1
            x[1] = -1
print(count,klast)