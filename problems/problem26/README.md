# Reciprocal Cycles

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 
to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring 
cycle in its decimal fraction part.

## Solution

To solve this problem I used the remainder from each step in long division 
to search 
for cycles. The calculated remainder is stored in a set and if the 
number already exists in the set, the cycle length is calculated.
If the remainder ever reaches zero, a cycle does not exist and 
the number can be safely ignored. For example, lets step through d = 4...

1. 1 / 4 = 0 remainder 1. This step is always the same since we are only 
    dealing with numbers < 1.
2. 10 / 4 = 2 remainder 2. Remember that in long division at each step you 
    bring down the next digit, which, in this case, is always 0. Thus, the new 
    denominator is 10 (1 * 10).  Since our remainder at this step is 2, 
    the denominator at the next step will be 20 (2 * 10).
3. 20 / 4 = 4 remainder 0.  Since we have reached a 0 in the remainder, the 
    calculation stops and we can ignore d = 4.
    
Next, lets look at a case that contains a cycle. d = 7.

1. 1 / 7 = 0 remainder 1.
2. 10 / 7 = 1 remainder 3.
3. 30 / 7 = 4 remainder 2.
4. 20 / 7 = 2 remainder 6.
5. 60 / 7 = 8 remainder 4.
6. 40 / 7 = 5 remainder 5.
7. 50 / 7 = 7 remainder 1.  Since we have already calculated 1 as a remainder
    in step 1, we can stop and return the cycle length 6.
    
The next step is to calculate the cycle length. For some values of d, there are
initial numbers not included in the cycle.  For example, 1 / 6 = 0.1(6). The 1 
must not be counted in the cycle length. This is performed by using the 
remainder set to determine the first index of the cycle and subtracting the 
number of digits not in the cycle.

Since the algorithm continues to iterate until 0 or a repeated remainder is 
reached, if a cycle exists, the maximum cycle length will be d - 1.  Following
the idea that the maximum cycle length is d - 1, this biases larger numbers.  
In addition, for any number n with cycle length m, any number less than m 
will never have a cycle length greater than m.  This realization can allow 
the algorithm the terminate early.  Since larger numbers are biased, the 
algorithm starts at 1000 and counts down.  When d becomes less than the max
cycle length, the algorithm terminates.
