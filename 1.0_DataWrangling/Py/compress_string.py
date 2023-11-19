""" In this task, we would like for you to appreciate the usefulness 
of the groupby() function of itertools.
You are given a string S. Suppose a character 'c' occurs consecutively
X times in the string. Replace these consecutive occurrences of 
the character 'c' with (X, c) in the string.
For a better understanding of the problem, check the explanation.

Input Format
A single line of input consisting of the string S.

Output Format
A single line of output consisting of the modified string.

Constraints
All the characters of S denote integers between 0 and 9.
1<=S<=(10)^4

Sample Input
1222311

Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)

Explanation
First, the character 1 occurs only once. It is replaced by (1, 1). 
Then the character 2 occurs three times, and it is replaced by (3, 2)
and so on.
Also, note the single space within each compression and between the compressions. """

from itertools import groupby

input_string = input()
result = []

for k, g in groupby(input_string):
    result.append((len(list(g)), int(k)))

print(*result)

# Note:
    # k is the key on which the grouping is done, in this case, it’s the character from the string. So, k is a single character and len(list(k)) will always be 1.
    # g is an iterator that generates the group of values. Converting it to a list with list(g) gives a list of all the consecutive occurrences of the character k in the string. So, len(list(g)) gives the number of these consecutive occurrences.