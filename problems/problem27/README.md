# Quadratic Primes

Euler discovered the remarkable quadratic formula:

n2+n+41

It turns out that the formula will produce 40 primes for the consecutive 
integer values 0≤n≤39. However, when 
n=40,40^2+40+41=40(40+1)+41 is divisible by 41, 
and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 
80 primes for the consecutive values 0≤n≤79. The product of the 
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, 
starting with n=0.


## Solution 

### Bruteforce

My bruteforce solution for this problem is to loop over all possible 
combinations of a and b for each combination, loop over increasing values of 
n until a non-prime is found. The product of a and b of the greatest value 
of n is returned.  Unfortunately, this solution would take a couple of minutes
to run due to having to check every prime value.

### Optimizations

The first optimization I made was to use a set of precomputed prime values and 
for each value of n, check for membership in this set to avoid running 
`is_prime` for every step since running `is_prime` is costly. In all honesty,
I assumed that the upper bound for the prime set would not be greater 
than 1000 which turned out to be correct.

### Going Further

After reading through the problem forum I realized I missed a number of key
realizations.  I implemented these optimizations in `further.py`.

1. b must be prime since for n = 0, n^2 + an + b = b so b must be prime.
2. b must be odd since for n = 2, n^2 + an + b = 4 + 2a + b so b must be odd.
3. a must be odd since for n =1, n^2 + an + b = 1 + a + b and b is odd. 
    b + 1 is even, thus, a must be odd.
4. The number of primes in a row cannot be greater than b - a since 
    <p style:"text-align: center;">n^2 + an + b =</p>
    <p style:"text-align: center;">(b - a)n^2 + a(b - a) + b =</p>
    <p style:"text-align: center;">b(b - a + 1) which is divisible by b.</p>
    Using the bounds |a| < 1000 and |b| ≤ 1000, the maximum number of primes
    that should be added to the prime set is 999 - -1000 = 1999.
    

## Lessons

* Pay more attention to the maths.