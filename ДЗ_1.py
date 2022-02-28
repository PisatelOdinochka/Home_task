duration = ' '

while duration:
    duration = int(input('Enter duration:'))
    second = duration
    
    minute = 0
    while second >= 60:
        minute += 1
        second = second - 60

    hour = 0
    while minute >= 60:
        hour += 1
        minute = minute - 60

    day = 0
    while hour >= 24:
        day += 1
        hour = hour - 24
        

    if duration >= 0 and duration < 60:
        print(str(second) + ' sec')
    elif duration >= 60 and duration< 3600:
        print (str(minute) + ' min ' + str(second) + ' sec ')
    elif duration >= 3600 and duration< 86400:
        print (str(hour) + ' h ' + str(minute) + ' m ' + str(second) + ' s ')
    elif duration >= 86400:
        print (str(day) + ' d ' + str(hour) + ' h ' + str(minute) + ' m ' + str(second) + ' s ')
    else:
        print ('error')