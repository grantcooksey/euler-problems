# Distinct Powers

Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

<p style="text-align: center;">2^2=4, 2^3=8, 2^4=16, 2^5=32</p>
<p style="text-align: center;">3^2=9, 3^3=27, 3^4=81, 3^5=243</p>
<p style="text-align: center;">4^2=16, 4^3=64, 4^4=256, 4^5=1024</p>
<p style="text-align: center;">5^2=25, 5^3=125, 5^4=625, 5^5=3125</p>
If they are then placed in numerical order, with any repeats removed, we get 
the following sequence of 15 distinct terms:

<p style="text-align: center;">4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 
625, 1024, 3125</p>

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 
and 2 ≤ b ≤ 100?


## Solution 


The solution uses a nested loop to calculate all the combinations and adds 
each combination value to a set.  The length of the set is returned once the 
loops are finished.

##

* In the CPython implementation, len() is O(1) for sets.