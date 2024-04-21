#1
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    prime_numbers = generate_primes(20)
    with open("ppp.txt", "w") as file:
        for prime in prime_numbers:
            file.write(str(prime) + "\n")
    print("20 liczb pierwszych zostalo zapisanych do pliku ppp.txt")

#2
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

if __name__ == "__main__":
    fibonacci_numbers = generate_fibonacci(20)
    with open("fff.txt", "w") as file:
        for number in fibonacci_numbers:
            file.write(str(number) + "\n")
    print("20 liczb ciagu fibonacciego zostało zapisanych do pliku fff.txt")

#3
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factors.append(n)
            break
    return factors

if __name__ == "__main__":
    with open("fff.txt", "r") as file:
        numbers = [int(line.strip()) for line in file]

    factors_list = [prime_factors(number) for number in numbers]

    with open("zzz.txt", "w") as file:
        for factors in factors_list:
            file.write(" ".join(map(str, factors)) + "\n")

    print("Czynniki pierwsze liczb z pliku fff.txt zostaly zapisane do pliku zzz.txt")
#4
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    prime_count = 0
    with open("zzz.txt", "r") as file:
        for line in file:
            numbers = map(int, line.strip().split())
            for number in numbers:
                if is_prime(number):
                    prime_count += 1

    print("Liczba liczb pierwszych w pliku zzz.txt:", prime_count)
