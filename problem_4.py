# Solving projecteuler.net/problem=4
# General Problem Description: Find the largest palindrome made from the product of two three digit numbers

# Determines if an integer is a palindrome
# input: number to check
# output: True if number is palindrome, false otherwise
def is_palindrome(num):
    to_check = str(num)
    for x in range(0, len(to_check) // 2):
        if to_check[x] != to_check[(-1 * (x+1))]:
            return False
    return True

def main():
    starting_num = 999
    found = False

    for sub_pool in range(0, 2*starting_num):
        midpoint = sub_pool // 2 # floor divide
        for difference in range(0, midpoint):
            potential_palindrome = (starting_num-(midpoint - difference)) * \
                                    (starting_num-(midpoint + difference))
            
            if is_palindrome(potential_palindrome):
                found = True
                print(potential_palindrome)
                break

        if found:
            break

if __name__ == "__main__": 
    main()
