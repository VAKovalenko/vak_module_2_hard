def get_cipher(number):
    '''
    Эта функция принимает число и генерирует шифр из пар чисел друг за другом, таких,
    что входное число было кратно(делилось без остатка) сумме их значений.
    :param number: number
    :return: cipher
    '''
    cipher = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                cipher += str(i) + str(j)
    return cipher

n = int(input('Введите целое число от 3 до 20: '))
if n < 3 or n > 20:
    print ('Число должно быть от 3 до 20, перезапустите программу.')
else:
    result = get_cipher(n)
    print('Шифр:', result)
