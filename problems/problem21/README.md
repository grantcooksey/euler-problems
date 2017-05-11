# Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

# Bruteforce Racket Solution

The bruteforce solution starts by creating a list of the sums of each numbers divisors then checks each number to see if that number has an amicable pair.  If a amicable pair is discovered, the number is left as its own value. Otherwise, if no pair is found, the number is set to zero.  Finally, this list is summed to get the ansIr.

I am not sure what the proper convention should be for amicable pair search.  The index of the current number is passed recursively but this does not feel very lispy(:question:) but I couldn't think of a better. It's basically a map but needs the current number's index.  Potentially this could be done away with by earmarking both numbers in the pair to prevent having to look backward when reaching the second pair.

# Bruteforce Python Solution

I wanted to learn a bit more about some python data structures and features that I use less often yet still remain performant.
The idea is the same as the racket solution where the list of sums of divisors is first generated and the amicable
pairs are discovered by iterating through the list a second time and summing the pairs. At first, I started with a 
numpy array using `vectorize` to create the array of sums of divisors but this approach ended up being quite slow.
I still am not too sure why this was the case and needs further exploration. I compared my code against a [blog](http://code.jasonbhill.com/c/project-euler-problem-21/) post
which I considered to be the most obvious and efficient bruteforce solution. I decided to use a generator to create
the sum-divisor list so that the list could be traversed lazily.  In Jason's solution, the list is traversed twice,
the first time to build the list of summed divisors and the second to discover the amicable pairs.  Since I used a 
generator, I am doing the same amount of work in a single traversal.  Since I am looking for pairs, the index and the 
divisor summation from the first number
in the pair will be stored in the dictionary and when the second number is reached, it will check the dictionary to 
discover the first number.  Finally, both numbers will be added to the sum.  This method prevents me from having to worry about
numbers going out of bounds.  Since numbers are their associated divisor sums may conflict with each other, the dictionary
must store the divisor sums within a set to avoid overwriting a divisor sum.  Since we are looking for pairs, we do not
have to worry about conflicts within the sets.


The advantages of this method is that it conserves memory over Jason's approach since the dictionary is pruned at each 
iteration but the disadvantage is that the code is more complex and runs a hair slower due to the cost of checking for 
membership, insertion, and deletion within the sets and the dictionary.  That being said, since get, insertion, and 
deletion are O(1) for [dictionaries and sets](https://wiki.python.org/moin/TimeComplexity), this gives O(n^2)
complexity for both solutions, ie. a summation of sums.

# Optimization

I derived the optimized solution with the help of the explanation provided by PE(project euler).  Their solution is 
interesting because it conserves memory by not utilizing any data structures in the outer loop to find amicable pairs.
In this case, there is a very slight trade-off between speed and memory usage between PE's solution and mine.  PE's
solution is **very slightly** slower because they calculate the sum of divisors twice where my solution calculates
it once and stores the value.  I prefer their solution better since it is much more elegant.

The main optimization comes from making more efficient methods of calculating the sum of divisors for a number.  I 
understood that the upper bound of numbers that you need to check was the floor of the square root of the given 
number but I missed the realization that odd number cannot have even divisors.  This improves the solution from O(n^2) 
to O(sqrt(n)*n).

# Prime Factorization

[Proof](http://planetmath.org/formulaforsumofdivisors).

# Lessons

* `Let` is **Awesome**!!!! :heart_eyes: :heart_eyes: Local binding makes debugging much easier and allows me to avoid defining as many top level functions.
* Be aware that using vectorized code is not always performant.  I need to look into this more to understand what is going on.
* Odd numbers cannot have even numbers as divisors.