# Solving projecteuler.net/problem=2
# General Problem Description: Sum the even valued Fibonacci numbers below 4,000,000

number_one = 1
number_two = 2

sum_evens = 2

while number_two < 4000000:
    new_number = number_one + number_two
    if new_number % 2 == 0:
        sum_evens = sum_evens + new_number
    
    #update fibonacci
    number_one = number_two
    number_two = new_number

print(sum_evens)
