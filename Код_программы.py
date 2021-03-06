import random #импорт модуля random
#Ввод и проверка значения k
while True :
    try:      
        k = int(input('Введите натуральное число k<8 :'))
    except ValueError: 
        k = 'error'
            
    if k == 'error':
        print('Попробуйте еще раз.')
        continue
    elif k < 1 :   
        print('Число должно быть больше 0')
        continue
    elif k > 8 :
        print('Число не должно быть больше 8')
        continue
    else :
        break  
#Ввод и проверка значения l    
while True :
    try:      
        l = int(input('Введите натуральное число l<8 :'))
    except ValueError: 
        l = 'error'
            
    if l == 'error':
        print('Попробуйте еще раз.')
        continue
    elif l < 1 :   
        print('Число должно быть больше 0')
        continue
    elif l > 8 :
        print('Число не должно быть больше 8')
        continue
    else :
        break    
#Ввод и проверка значения m
while True :
    try:      
        m = int(input('Введите натуральное число m<8 :'))
    except ValueError: 
        m = 'error'
            
    if m == 'error':
        print('Попробуйте еще раз.')
        continue
    elif m < 1 :   
        print('Число должно быть больше 0')
        continue
    elif m > 8 :
        print('Число не должно быть больше 8')
        continue
    else :
        break    
#Ввод и проверка значения n
while True :
    try:      
        n = int(input('Введите натуральное число n<8 :'))
    except ValueError: 
        n = 'error'
            
    if n == 'error':
        print('Попробуйте еще раз.')
        continue
    elif n < 1 :   
        print('Число должно быть больше 0')
        continue
    elif n > 8 :
        print('Число не должно быть больше 8')
        continue
    else :
        break
    
#Проверка цвета поля. Если сумма координат поля четное число, то поле черное, если нет - белое.
if (k+l)%2 == 0:
    print('Поле (', k,',',l, ') - черное.')
else:
    print('Поле (', k,',',l, ') - белое.')
    
if (m+n)%2 == 0:
    print('Поле (', m,',',n, ') - черное.\n')
else:
    print('Поле (', m, ',', n, ') - белое.\n')

#Проверка, может ли ферзь попасть на поле (m,n) 
#Если модули разностей координат равны или k==m или l==n, то ферзь угрожает заданному полю.
if abs(k-m) == abs(l-n) or k == m or l == n:
    print('Ферзь на поле (', k,',',l, ') угрожает полю (', m,',',n ,')\n',)
#Если условие выше не выполняется, то ферзь не может одним ходом попасть на заданное поле
#Чтобы попасть на заданное поле, подбирается такой ход, чтобы хотя бы одна 
#из его координат совпадала с координатами предыдущего поля и чтобы совпадала их разность или сумма
else:
    print('Ферзь на поле (', k, ',', l, ') не угрожает полю (', m,',',n ,')',)
    k1 = random.randint(1,8)
    l1 = random.randint(1,8)
    while not((k==k1 or l==l1) and (m-n == k1-l1 or m+n == k1+l1)):
        k1 = random.randint(1,8)
        l1 = random.randint(1,8)
    print('Чтобы ферзь попал на поле (', m,',',n ,') можно сделать ход на поле (', k1,',',l1, ')\n')

#Если при уменьшении или увеличении координаты k на 1, она совпадает с координатой m, и при уменьшении или увеличении координаты l на 2, она совпадает с n
#(И наоборот) то конь с одного хода может попасть на заданное поле 
if (k - 1 == m or k + 1 == m) and (l - 2 == n or l + 2 == n):
    print('Конь на поле (', k,',',l, ') угрожает полю (', m,',',n ,')\n',)
elif (k - 2 == m or k + 2 == m) and (l - 1 == n or l + 1 == n):
    print('Конь на поле (', k,',',l, ') угрожает полю (', m,',',n ,')\n',)
#Иначе конь не может попасть на заданное поле с одного хода
else:
    print('Конь на поле (', k,',',l, ') не угрожает полю (', m,',',n ,')\n',)

#Если хотя бы одна из координат ладьи совпадает с координатами заданного поля, то ладья может попасть на это поле
if k==m or l == n:
    print('Ладья может одним ходом попасть на поле (', m,',',n ,')\n',)
#Если ладья не может попасть на заданное поле с одного хода, то следующий ход должен быть таким, чтобы с предыдущим ходом совпадала хотя бы одна координата.
else:
    print('Ладья не может одним ходом попасть на поле (', m,',',n ,')',)
    print('Чтобы ладье попасть на поле (', m,',',n ,') нужно:\n1)Сделать ход на поле (', m,',',l, ') или (', k,',',n, ') \n2)Затем на поле (', m,',',n ,')\n')

#Если модули разностей координат равны, то Слон с одного хода может попасть на заданное поле
if abs(k - m) == abs(l - n):
    print('Слон на поле (', k,',',l, ') угрожает полю (', m,',',n ,')\n',)
    
#В ином случае нужно проверить, одного ли цвета заданные поля, если нет, то на заданное поле слону попасть невозможно
#Если же поля одного цвета, то нужно, чтобы сопадала разность или сумма координат следующего и предыдущего полей
#и сумма или разность следующего и конечного полей
else:
    print('Слон на поле (', k,',',l, ') не угрожает полю (', m,',',n ,')',)
    k1 = random.randint(1,8)
    l1 = random.randint(1,8) 
    if (k+l)%2 != (m+n)%2:
        print('Слон не может перейти на поле другого цвета. На поле (', m,',',n ,') попасть невозможно')
    else:
        while not((k-l == k1-l1 or k+l == k1+l1) and (m-n == k1-l1 or m+n == k1+l1) and ((k+l)%2 == (k1+l1)%2)):
            k1 = random.randint(1,8)
            l1 = random.randint(1,8)
        print('Чтобы слон попал на поле (', m,',',n ,') можно сделать ход на поле (', k1,',',l1, ')')

