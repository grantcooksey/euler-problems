# Digit Fifth Powers

Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

<p style="text-align: center;">1634 = 1^4 + 6^4 + 3^4 + 4^4</p>
<p style="text-align: center;">8208 = 8^4 + 2^4 + 0^4 + 8^4</p>
<p style="text-align: center;">9474 = 9^4 + 4^4 + 7^4 + 4^4</p>

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth 
powers of their digits.


## Solution 


The solution first finds the upper bound of possible numbers. Since the sum of 
powers grows at a constant rate for each additional digits contrasted with 
adding a digits, which grows exponentially at a factor of 10, there is an 
upper bound for the power sum. The bruteforce solution iterates through the 
numbers 2 to the upper bound and check if the sum of powers for each number
is equal to the number.  Avoiding string conversion significantly speeds up
the computation.