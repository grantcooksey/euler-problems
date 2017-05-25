# Circular Primes

The number, 197, is called a circular prime because all rotations of the 
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 
71, 73, 79, and 97.

How many circular primes are there below one million?


## Solution 


The solution first generates a list of all primes under 1000000 and places
them in a set since we are only looping through the numbers and testing for 
membership. For each number under 1000000, we test if it is circular by 
dividing by 10^(number of digits - 1) to get the first digits and then 
testing if the remainder * 10 + first digit is prime. This is repeated until 
all digits have cycled through.


## Lessons


* Sieve of Eratosthenes - see problem 10