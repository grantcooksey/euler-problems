# Truncatable Primes

The number 3797 has an interesting property. Being prime itself, it is possible 
to continuously remove digits from left to right, and remain prime at each 
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 
379, 37, and 3. 

Find the sum of the only eleven primes that are both truncatable from left to 
right and right to left. 

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes. 


## Solution


The solution finds a set of primes using a sieve and loops through each prime
in the set checking if the prime is both right and left truncatable. Standard
division and modulus operations are used to pull digits out to check for left
truncatable primes. At each step, the current number is checked to see if it 
is prime using the prime set. A stack is used to check for right truncatable 
primes. The number is split into digits and added to the stack. As numbers are
popped off, they are multiplied by 10 raised by the number of numbers left on 
the stack and subtracted from the current number. This removes the first digit
from the current number and it is checked to see if it is prime.

I attempted to optimize the problem by filtering all primes where the first 
digit was not prime but although this significantly reduced the number of 
primes in the set, it still required a loop over all thr primes and the
truncatable prime check was relatively inexpensive so the speedup was 
negligible.

I was not able to find a way to prove that the upper bound from truncatable
primes is 739397 so I chose an arbitrarily large number when creating the 
sieve. 
