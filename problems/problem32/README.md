# Pandigital Products

We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.

## Solution 


### Bruteforce

The bruteforce solution creates a list of all possible multiplicand and 
multiplier indexes for a list 1-9 and for each pair, it iterates over 
all permutations of the a list of numbers 1-9.  If a pandigital number 
is discovered, it is added to a set.  The sum of the set is returned.

This solution is incredibly slow (~30 seconds).

### Optimized

The optimized solution filters out all the impossible lengths for the
multiplier and multiplicand. The intuition is that only possible pairs
for valid lengths of the multiplicand and the multiplier are
* 1 and 4
* 2 and 3
All permutations are searched, but for each permutation, only values with
these two lengths for the multiplicand and multiplier are checked.  This 
gave a drastic speedup (~1 second).