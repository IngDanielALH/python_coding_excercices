"""
In Amazon Go Store, there are n items, each associated with two positive values a[i] and b[i]. There are infinitely
many items of each type numbered from 1 to infinity and the item numbered j of type i costs a[i]+(j−1)∗b[i] units.

Determine the minimum possible cost to purchase exactly m items.

Example Given n=3, a=[2,1,1], b=[1,2,3], m=4

The optimal types to buy are:

    Choose i=1. This is the first purchase of this type of item, so j=1.
    The first item costs a[1]+(1−1)∗b[1]=1+(1−1)∗2=1.

    Choose i=2. Again, it is the first purchase of this type so j=1. The second item costs 1+(1−1)∗3=1.

    Choose i=0 which costs 2+(1−1)∗1=2.

    When a second unit of any type is purchased, j=2 for that transaction. The costs of a second units of each item are:

        a[0] costs a[0]+(2−1)∗b[0]=2+1∗1=3

        a[1] costs 1+1∗2=3

        a[2] costs 1+1∗3=4

        Choose either a[0] or a[1] since they cost less.

The total cost to purchase is 1+1+2+3=7.

Function Description Complete the function getMinimumCost in the editor below.

getMinimumCost has the following parameters:

    int a[n]: an array of integers

    int b[n]: an array of integers

    m: the number of items to purchase

Returns

    long integer: the minimum cost
"""