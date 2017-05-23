# Digit Cancelling Fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which 
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less 
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.


## Solution 


The solution was to loop over all the possible values and manually check
each for matching digits and equality when divided against the original 
fraction.  Not going to improve further since it already runs very quickly.


## Lessons


* [Explanation of GCD](https://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python)