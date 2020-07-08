"""
Example with total lambs
of 10.

Time complexity: O(n)
Generous logic: (2^k)
h0 = 1
h1 = 2
h2 = 4

Time complexity: O(n)
Stingy logic: (fib)
h0 = 1
h1 = 1
h2 = 2
h3 = 3

"""

def solution(total_lambs):
    
    #Generous
    generous_henchman = 1
    generous_lambs = total_lambs
    generous_count = 0

    while(generous_lambs > 0):
        generous_henchman = generous_henchman << 1
        generous_count += 1
        generous_lambs -= generous_henchman


    #Stringy
    stringy_henchman_0 = 1
    stringy_henchman_1 = 1

    c = 0
    stringy_count = 1

    stringy_lambs = total_lambs
    # The first two henchmans are always set to 1
    stringy_lambs -= 2

    while c <= stringy_lambs:
        next_henchman = stringy_henchman_0 + stringy_henchman_1

        stringy_henchman_0 = stringy_henchman_1
        stringy_henchman_1 = next_henchman

        stringy_count += 1
        c += next_henchman

    return abs(generous_count - stringy_count)