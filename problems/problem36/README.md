# Double-base Palindromes

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)


## Solution 


### Bruteforce

The bruteforce solution checks each number under 1000000 to see if itself
and its binary equivalent are palindromes.  Since Python has a built-in
function `bin()` which converts a number into its binary equivalent, the
method `palindrome(s)` takes a string.  This mean that each number must be
converted to a string. As noted in previous problems, this conversion is
expensive but I decided to use it for simplicity since `bin()` returns a
string.


### Optimized

An easy optimization is to only check palindromes under 1000000.  Since the
palindromes
are the same forwards and backwards, the solution only needs to generate
the first half of the number to find a palindrome.  The solution does so
by generating all permutations with repetition of lengths less than 3 since
we will not check any palindrome greater than 999999, which has 6 digits.
In the case of palindromes with an odd number of digits, each permutation
will be created into a group of palindromes with the middle numbers from 1
to 9. These will then be checked to see if their binary equivalents' are
palindromes.
