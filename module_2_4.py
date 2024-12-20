numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers: # Исключение числа 1 из списка
    if number == 1:
        continue
    is_prime = True
    for divisor in range(2, number): # Вложенный цикл для подбора делителей 1 числа
        if number % divisor == 0:
            is_prime = False
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
print("Простые числа:", primes)
print("Не простые числа:", not_primes)




