# Number Spiral Diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 
5 by 5 spiral is formed as follows:

**21** 22 23 24 **25**
20  **7**  8  **9** 10
19  6  **1**  2 11
18  **5**  4  **3** 12
**17** 16 15 14 **13**

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?


## Solution 


At each ring level in the square, the upper right corner number is given by
the formula (2(level + 1) - 1)^2 assuming the center number is level 0. There 
is a fixed space between any corner number and the two corners on either side 
that is (2*level + 1) spaces.  Using these two equations, for each level, the
corner is calculated and the fixed space is subtracted four times to get the
values of all four corners.  This value is then added to the sum of numbers 
on the diagonals until the upper right corner becomes greater than 1001^2.


## Lessons


* Step through your program before submitting!!! I submitted early with an 
    obvious bug that I would have caught had I stepped through the code first. 