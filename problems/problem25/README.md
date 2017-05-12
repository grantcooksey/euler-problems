# 1000-digit Fibonacci Number

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
, F2 = 1
, F3 = 2
, F4 = 3
, F5 = 5
, F6 = 8
, F7 = 13
, F8 = 21
, F9 = 34
, F10 = 55
, F11 = 89
, F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

## Solution

### Bruteforce

This problem was relatively easy to solve using python due to the fact that `int` to `long` conversion happens
automatically and `long` is only constrained by available memory, allowing me to use very large numbers without 
having to worry about accuracy and type conversion.

The bruteforce solution operates by iterating through all fibonacci numbers until the first one is found with 
1000 digits.  This solution could be written concisely in a recursive fashion but the recursion level would be 
 very deep so I chose to approach the problem using an iterative approach.

I discovered a way to mathematically calculate how many digits are in a number using log base 10.  I think this method is superior
to my previous method of converting to a string and counting the length of the string because the conversion
from an `int` to `str` is slow for large numbers.  I think that the string conversion method is more readable but
this method outperformed the string conversion by a factor of ~20 for this problem.

The formula to calculate digits is 
<p style="text-align: center;">`digits = math.floor(math.log10(n)) + 1`</p>

### Binet's Formula

I found this solution by looking through the forums.

Description of the maths [here](http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html)

## Lessons

* In python, `int` is of a limited size and `long` is based on available memory.  Conversion happens when 
necessary.
* Use `digits = math.floor(math.log10(n)) + 1` to calculate number of digits for large numbers.