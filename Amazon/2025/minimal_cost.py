"""
A Category Manager at Amazon has noticed that one of the products listed is available in n sizes, represented by the
array size. However, some of these sizes are repetitive, which creates a poor user experience. To optimize inventory
and clarity, the product should be available in distinct sizes only.

Problem Statement You are given two integer arrays, size and cost, both of length n.

    size[i] represents the current size of the ith product.

    cost[i] represents the cost to increase the size of the ith product by 1 unit.

You can increase the size of any product as many times as needed to ensure all sizes in the array are unique. The cost
of increasing a size from Sold to Snew is calculated as:
TotalCost=cost[i]×(Snew−Sold)

Find the minimum total cost required to make all elements in the size array distinct.

Function Description Complete the function getMinimumCost which takes the following parameters:

    int size[n]: The current sizes of the products.

    int cost[n]: The costs to increment the size of each product.

Returns

    long integer: The minimum total cost to make all sizes distinct.

Example

Input:

    n=4

    size=[2,3,3,2]

    cost=[2,4,5,1]

Step-by-Step Analysis: The initial sizes are [2, 3, 3, 2]. We have duplicates at value 2 (indices 0 and 3) and value 3
(indices 1 and 2).

Optimal Strategy:

    Resolve duplicate '3':

        Target size[1] (value 3, cost 4).

        Increase it to 4.

        Cost incurred: 4×(4−3)=4.

        New sizes: [2, 4, 3, 2].

    Resolve duplicate '2':

        Target size[3] (value 2, cost 1).

        Notice we cannot change it to 3 or 4 because those are now taken. The next available distinct integer is 5.

        Increase size[3] from 2 to 5.

        Cost incurred: 1×(5−2)=3.

        New sizes: [2, 4, 3, 5].

Total Cost: 4+3=7.

Alternative (Sub-optimal) Strategy: If we had instead moved size[1] to 5 (cost 4×2=8) and size[3] to 4 (cost 1×2=2),
the total would be 10, which is higher than 7.

Output: 7
"""