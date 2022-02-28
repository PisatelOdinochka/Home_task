my_list = []

my_suma = []  #Ввел этот список, так как проссматривать данные в списке удобнее


for i in range(1, 1000):
    if i % 2 == 1:
        i=i**3
        my_list.append (i)
            
        sum = 0
        while i > 0:
            digit = i % 10
            sum = sum + digit
            i = i // 10

        if sum % 7 == 0:
            my_suma.append (sum)
            
                        
print(my_list, """

    """)
print (my_suma)

for i in range(1, 1000):
        if i % 2 == 1:
            i=i**3
            my_list.append (i)
                
            sum = 0
            while i > 0:
                digit = i % 10
                sum = sum + digit
                i = i // 10

            if sum % 7 == 0:
                my_suma.append (sum)

print(my_list, """

    """)

print (my_suma, """
    """)            
        
i = 0
for i in range(0, len(my_list)):
    my_list[i] = my_list[i] + 17

                    
    sum = 0
    while i > 0:
        digit = i % 10
        sum = sum + digit
        i = i // 10

    if sum % 7 == 0:
        my_suma.append (sum)
                            
print(my_list, """

    """)
print (my_suma)