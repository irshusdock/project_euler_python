# Solving projecteuler.net/problem=5
# General Problem Description: What is the smallest positive number that is evenly divisible by all nums 1-20


prime_numbers = [2]

# determine the prime factors of a number
# input: the number to factorize
# output: a dict of prime number to number of times it exists as a factor
def prime_factorization(number):
    factorization = {}
    is_prime = True
    while number != 1:
        for prime in prime_numbers:
            if number % prime == 0:
                number = number / prime
                if prime in factorization:
                    factorization[prime] = factorization[prime] + 1
                else:
                    factorization[prime] = 1
                is_prime = False
                break
        # because we are calling prime_factorization on sequential numbers,
        # if the number doesn't have any factors from our prime_numbers list,
        # it MUST be prime
        if is_prime:
            prime_numbers.append(number)
            # not breaking here causes us to make one more pass through
            # prime_numbers but slightly simplifies later code
    return factorization

def main():
    prime_factors = [2] 
    last_number = 20

    for x in range(2, last_number + 1):
        factors = prime_factorization(x)
        for prime in factors:
            for y in range(0, factors[prime] - prime_factors.count(prime)):
                prime_factors.append(prime)
                   
    product = 1
    for prime in prime_factors:
        product = product * prime

    print(product)

if __name__ == "__main__": 
    main()
