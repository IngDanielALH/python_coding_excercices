"""
You are shopping on Amazon.com for some bags of rice. Each listing displays the number of grains of rice that the bag
contains. You want to buy a perfect set of rice bags from the entire search results list, riceBags. A perfect set of
rice bags, perfect, is defined as:The set contains at least two bags of rice.When the rice bags in the set perfect are
sorted in increasing order by grain count, it satisfies the condition:

perfect[i] * perfect[i] = perfect[i+1] for all 1 <= i < n

Here n is the size of the set and perfect[i] is the number of rice grains in bag i.Find the largest possible set
perfect and return an integer, the size of that set. If no such set is possible, then return -1.
It is guaranteed that all elements in riceBags are distinct.

Example
Let the bags of rice available on Amazon have grain
counts [3, 9, 4, 2, 16].
The following are the perfect sets:Set perfect = [3, 9]. The size of this set is 2.
Set perfect = [4, 2]. The size of this set is 2. (Note: When sorted it becomes [2, 4]).Set perfect = [4, 16].
The size of this set is 2.Set perfect = [4, 2, 16]. The size of this set is 3. (Note: When sorted it becomes [2, 4, 16],
and $2*2=4$, $4*4=16$).The size of the largest set is 3.
"""