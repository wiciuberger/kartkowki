#WERSJA 1

#1
# import random

# n = 10  # Liczba losowych elementów
# min_value = 1
# max_value = 100  # Zakres od min do max

# random_array = [random.randint(min_value, max_value) for _ in range(n)]
# print(random_array)
# #2
# array = [1, 1, 1, 5, 5, -2, 10, 1]

# max_value = max(array)
# min_value = min(array)

# print("Największa wartość:", max_value)
# print("Najmniejsza wartość:", min_value)
# #3
# def count_occurrences(arr, element):
#     return arr.count(element)

# array = [1, 1, 1, 5, 5, -2, 10, 1]
# element_to_count = 1
# occurrences = count_occurrences(array, element_to_count)

# print(f"{element_to_count} powtórzyło się {occurrences} razy.")

# #4
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# array = [2, 3, 4, 5, 6, 7, 8, 9]

# prime_numbers = [num for num in array if is_prime(num)]
# print("Liczby pierwsze w tablicy:", prime_numbers)

# #5
# n = 5
# array = [1, 3, 4, 6, 2, 8, 7]

# new_array = [x for x in array if x < n]
# print("Nowa tablica:", new_array)

# #6
# n = int(input("Ile liczb chcesz wprowadzić: "))

# even_numbers = []
# for i in range(n):
#     number = int(input(f"Podaj liczbę {i + 1}: "))
#     if number % 2 == 0:
#         even_numbers.append(number)

# print("Liczby parzyste:", even_numbers)

#WERSJA 2

#1
# A = [14, 21, 28, 36, 42, 49, 50, 63, 70]
# divisible_by_7_1 = [x for x in A if x % 7 == 0]
# divisible_by_7_2 = [x for x in A if x % 7 == 0]
# print("Pierwsza tablica:", divisible_by_7_1)
# print("Druga tablica:", divisible_by_7_2)

# #2

# a = 7
# sum_divisible_by_a = sum([x for x in A if x % a == 0])
# print("Suma liczb podzielnych przez", a, "to:", sum_divisible_by_a)

# #3

# x = 28
# count_x = A.count(x)
# print(x, "powtarza się", count_x, "razy w tablicy.")

# #4
# min_value = min(A)
# min_indexes = [i for i, x in enumerate(A) if x == min_value]
# print("Minimalne wartości znajdują się pod indeksami:", min_indexes)

# #5
# def harmonic_mean(numbers):
#     return len(numbers) / sum(1 / x for x in numbers)

# A = [2, 4, 9]
# harmonic_avg = harmonic_mean(A)
# print("Średnia harmoniczna:", harmonic_avg)

# #6
# import math

# A = [1, 4, 9, 16, 25, 36, 49]
# int_sqrt_numbers = [x for x in A if math.isqrt(x) ** 2 == x]
# print("Liczby, których pierwiastek jest liczbą całkowitą:", int_sqrt_numbers)

# WERSJA 3

# #1
# AAA = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# #2
# def harmonic_mean(numbers):
#     return len(numbers) / sum(1 / x for x in numbers)

# harmonic_avg = harmonic_mean(AAA)
# print("Średnia harmoniczna:", harmonic_avg)

# #3
# odd_numbers = [x for x in AAA if x % 2 != 0]
# print("Liczby nieparzyste:", odd_numbers)

# #4
# import random

# n = 10
# segment = list(range(n))
# random.shuffle(segment)

# part1 = segment[:n // 3]
# part2 = segment[n // 3:2 * n // 3]
# part3 = segment[2 * n // 3:]

# is_valid_split = len(part1) == len(part2) == len(part3) == n // 3
# print("Podział jest poprawny:", is_valid_split)
# #5
# n = 7
# indexes = [i for i, x in enumerate(AAA) if x == n]
# print(f"Element {n} znajduje się pod indeksami:", indexes)

# #6
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# prime_numbers = [x for x in AAA if is_prime(x)]
# print("Liczby pierwsze w tablicy:", prime_numbers)

