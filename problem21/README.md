# Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

# Bruteforce Racket Solution

The bruteforce solution starts by creating a list of the sums of each numbers divisors then checks each number to see if that number has an amicable pair.  If a amicable pair is discovered, the number is left as its own value. Otherwise, if no pair is found, the number is set to zero.  Finally, this list is summed to get the answer.

I am not sure what the proper convention should be for amicable pair search.  The index of the current number is passed recursively but this does not feel very lispy(:question:) but I couldn't think of a better. It's basically a map but needs the current number's index.  Potentially this could be done away with by earmarking both numbers in the pair to prevent having to look backward when reaching the second pair.

## Lessons

* `Let` is **Awesome**!!!! :heart_eyes: :heart_eyes: Local binding makes debugging much easier and allows me to avoid defining as many top level functions.
* Test each new function thoroughly.  I still ran into issues where I didn't test using data from previous functions and it came back to bite me.
* Be aware that using vectorized code is not always preformat.  I need to look into this more to understand what is going on.