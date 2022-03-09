percent_list = [ ]

for i in range(1,101):
    percent_list.append(i)
    t = i % 10

    if i >= 10 and i <= 20 or i == 100:
        print (str(i) + ' Процентов')
    elif t == 1:
        print (str(i) + ' Процент')
    elif t >= 2 and t <= 4:
        print (str(i) + ' Процента')
    elif t >= 5 and t <= 9:
        print (str(i) + ' Процентов')
    elif i >= 10 and i <= 20 or i == 100:
        print (str(i) + ' Процентов')