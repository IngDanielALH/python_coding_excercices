"""
A team of developers at Amazon is working on a feature to evaluate password strength during user registration.
Analysts have determined that passwords containing personal information are insecure.

Problem Statement The feature checks for the presence of a specific reference string within the user's password.
A password is considered weak if the reference string can be found as a subsequence in any possible permutation of the password.

Your task is to determine the minimum total cost to remove characters from the password such that no permutation of the
remaining characters contains the reference string as a subsequence.

Each character from 'a' to 'z' has an associated removal cost, provided in an integer array cost of size 26
(where cost[0] is the cost for 'a', cost[1] for 'b', etc.).

Function Description Given the strings password, reference, and the array cost, calculate the minimum cost required.

Input Format

    password: A string representing the user's proposed password.

    reference: A string representing the personal information to avoid.

    cost: An array of integers representing the cost to remove each character ('a'-'z').

Notes

    Permutation: A rearrangement of the characters in the string.
    For example, permutations of "abc" include "cba", "bca", etc.

    Subsequence: A sequence derived from another sequence by deleting some or no elements without changing the order
    of the remaining elements. For example, "ace" is a subsequence of "abcde".

Example

Input:

    password = "adefgh"

    reference = "hf"

    cost = [1, 0, 0, 1, 4, 4, 1, 1, ...] (Assuming cost of 'f' is 4 and 'h' is 1 for this example).

Reasoning: We need to ensure that the characters in password cannot be rearranged to form the reference string "hf".

    The password contains both 'h' and 'f'.

    Since order doesn't matter (because we are checking all permutations), simply having the characters 'h' and 'f'
    available means we can form the subsequence "hf".

    To fix this, we must remove either all instances of 'h' OR all instances of 'f' from the password.

Possible Solutions:

    Remove 'h':

        New password: "adefg"

        Cost: 1

    Remove 'f':

        New password: "adegh"

        Cost: 4

Result: The minimum cost is 1 (by removing 'h').
"""