num = int(input('Введи первое число: '))
summ = 0
while num !=0:
    last_num = num % 10
    summ += last_num
    if last_num == 5:
        print('Обнаружен разрыв')
        break
    num //= 10
    print('Текущая сумма: ', summ)
print('\nИтоговая сумма равна: ', summ)

print()
