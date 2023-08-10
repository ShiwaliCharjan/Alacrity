def is_prime(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    if len(factors) == 2:
        return True, 'Prime!'
    else:
        return False, factors

def primes_in_range(min, max):
    primes = []
    for i in range(min, max + 1):
        prime, _ = is_prime(i)
        if prime:
            primes.append(i)
    return primes

def cli_interface():
    print('Welcome to the Prime Number Calculator!')
    print('Enter 1 to check if a number is prime')
    print('Enter 2 to find all prime numbers in a range')
    choice = input('Enter your choice: ')
    if choice == '1':
        n = int(input('Enter a number: '))
        prime, factors_or_string = is_prime(n)
        if prime:
            print(factors_or_string)
        else:
            print(factors_or_string)
    elif choice == '2':
        min = int(input('Enter the minimum value of the range: '))
        max = int(input('Enter the maximum value of the range: '))
        primes = primes_in_range(min, max)
        print(primes)
    else:
        print('Invalid choice')

cli_interface()
