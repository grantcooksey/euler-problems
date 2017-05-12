# Lexicographic Permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 
1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

<p style="text-align: center;">012   021   102   120   201   210</p>

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

## Solution

I skipped the bruteforce solution since I have solved similar problems in the past.

The basic idea is to split the total number of possible permutations into bins based on the number of items in the
permutation set.  The permutation that you are looking for will fall into one of these bins and you select the 
item in the set with the bin value and concatenate to the final permutation.  The permutation number is set to 
the difference between the number and the start of the current bin and the total is set the current size of the
bin.  This process is repeated until all items have been removed from the set. 

The worst case, building the permutation will take (10 * (10 + 1))/2 = 55 iterations.  This gives us a complexity 
of O(n^2) where n is the number of items in our permutation list.

## Lessons

* Permutations without repetitions in the factorial of the number.  Divide that by (n-r)! for the number of r 
length permutations.