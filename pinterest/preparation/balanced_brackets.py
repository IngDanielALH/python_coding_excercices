"""
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a
closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {},
and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is
not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single,
unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

    It contains no unmatched brackets.
    The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of
    brackets.

Given

strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES.
Otherwise, return NO.

Function Description

Complete the function isBalanced in the editor below.

isBalanced has the following parameter(s):

    string s: a string of brackets

Returns

    string: either YES or NO

Input Format

The first line contains a single integer
, the number of strings.
Each of the next lines contains a single string , a sequence of brackets.
"""


def test_case(message: str, expected: str, actual: str) -> None:
    if actual == expected:
        print(f"Test case: {message} SUCCESS")
    else:
        print(f"Test case {message}: FAILED")
        print(f"Expected {expected}, Got {actual}")
    pass


def isBalanced(s: str) -> str:
    brackets_pair = {'{': '}', '[': ']', '(': ')'}
    stack = []

    if len(s) % 2 != 0:
        return "NO"

    for char in s:
        if char in brackets_pair.keys():
            stack.append(char)
        elif brackets_pair[stack[-1]] == char:
            stack.pop()
        else:
            return "NO"

    return "YES"
    pass


if __name__ == '__main__':
    #test_case("Try test function", "YES", "YES")
    #test_case("Happy path", "YES", isBalanced("{[()]}"))
    #test_case("Incomplete str", "NO", isBalanced("{[()]"))
    #test_case("Not balanced", "NO", isBalanced("{([)]}"))
    test_case("Not closed", "NO", isBalanced("(()"))
    test_case("Pair not balanced", "NO", isBalanced("(("))

