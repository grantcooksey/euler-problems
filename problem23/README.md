# Non-abundant Sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, 
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this 
sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum 
of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can 
be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is 
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

## Bruteforce

The bruteforce solution first calculates all positive abundant numbers under 28123, the upper limit given in the 
problem description.  A boolean array of length 28123 is initialized all to true to represent the values that are 
not the sum of two abundant numbers. A nested loop then iterates each value of the known abundant numbers against itself and switches the boolean value in the non abundant number sum array if the sum of the current two abundant numbers are within the bounds of the array.  Finally, the non abundant sum array is iterated and the index of all true values are summed and the resulting sum is returned.

I tried a method where instead of initializing an addition deficient number boolean array, I used set 
comprehension to find all abundant numbers and used a for loop to check for membership in the set.  
This solution had a significant speedup.

### Optimizations

Off the top of my head, I see some obvious optimizations to the bruteforce solution.  The first realization 
is that the nested loop we are calculating each sum twice.  This could reduce the number of calculations from 
n^2 to (n^2 + n)/2 iterations(add n since we are including numbers that are the sum of the same abundant number).  
I am sure that PE will note this, but also we could start the abundant sum loop at 24 since that is the first 
number that is the sum of two abundant numbers(12 * 2).  Although the first optimization will cut calculation 
time roughly in half, it is still a topical improvement and would not scale well.  Not sure how to apply this 
to the set comprehension solution.

The second improvement off the bruteforce solution is early termination of the inner loop when the sum of the 
abundant numbers is greater than the max.  

## Lessons

* Set comprehension in python is fast.  The speed up was similar to using the optimized bruteforce solution with 
nested for-loops.  This speed up may be due to the cost of using an additional data structure to store deficient 
numbers
* **Remember to look for solutions that conserve memory!**