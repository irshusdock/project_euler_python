# Solving projecteuler.net/problem=3
# General Problem Description: What is the largest prime factor of 600851475143

prime_numbers = [2, 3, 5]
prime_factors = set([])

# add a new prime number to the list
def next_prime():
    test_num = prime_numbers[-1] + 1
    while True:
        # assume the current number is prime, if not increment the number and try again
        is_prime = True
        for prime in prime_numbers:
            if test_num % prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(test_num)
            break
        else:
            test_num = test_num + 1


# one step of the prime factorization process
# input: the number to factorize, the index in the prime_numbers list to start at
# output: the reduced number
def remove_factor(number, index):
    for x in range(index, len(prime_numbers)):
        if number % prime_numbers[index] == 0:
            prime_factors.add(prime_numbers[index])
            return number/prime_numbers[index]
    next_prime()
    return remove_factor(number, len(prime_numbers)-1)

def main():
    number = 600851475143
    while number != 1:
        number = remove_factor(number, 0)
    print(max(prime_factors))

if __name__ == "__main__":
    main()
