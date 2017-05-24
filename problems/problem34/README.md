# Digit Factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of 
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.


## Solution 


The solution first finds an upper bound to the and check to see if any number
below the upper bound is equal to the sum of the factorial of their digits.
The upper bound is found by finding the power of 10 that is greater than 9!
times the power.  Basically, at p = 7, 9! * p < 10^p - 1 and at
p = 6, 9! * p > 10^p - 1, placing the upper bound at 9! * 7 = 2540160.  

The solution runs relatively slow (~6 seconds) on my vm but I don't see any 
obvious optimizations.  My guess is that is it would be possible to build
a tree of possible values in sorted order and prune branches in blocks.  The 
leaves would then be traversed to find the values.