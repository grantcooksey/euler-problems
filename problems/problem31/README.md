# Coin Sums

In England the currency is made up of pound, £, and pence, p, and there are 
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?


## Solution 


### Bruteforce Using a Stack


The solution first places all the coin values on the stack along with their 
index
in the original coin list. For each coin value popped off the stack, if the 
coin value is less than the goal, which in our case is 200, a new item is 
created for each coin of equal and lesser value.  If the item popped off has 
a coin value greater than the goal, it is discarded. The new item coin value 
is the original coin value + the new coin and the index is the index of 
the last coin added.  For example if we have a list of coins \[1, 2, 5],
and a goal of 6 and we pop off an item with a coin value of 5 and an 
index of 2, since 5 < 6, we will add

* (5+5, 2)
* (5+2, 1)
* (5+1, 0)

to the stack. When each of these value are popped off, only the last item
will not be discarded. The number of items that were not discarded is 
returned.


## Lessons


* List any important lessons or tidbits that will be helpful in
the future in bullet form.