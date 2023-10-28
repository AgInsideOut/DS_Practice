""" itertools.combinations(iterable, r) 
This tool returns the r length subsequences of elements from the input iterable.
Combinations are emitted in lexicographic sorted order. So, if the input iterable 
is sorted, the combination tuples will be produced in sorted order.

Task:
You are given a string S. 
Your task is to print all possible combinations, up to size k, of the string S in lexicographic sorted order.

Input Format:
A single line containing the string S and integer value k separated by a space.

Constraints:
0 <= k <= len(S)
The string contains only UPPERCASE characters.

Output Format:
Print the different combinations of string S on separate lines.

Sample Input:
HACK 2

Sample Output:
A
C
H
K
AC
AH
AK
CH
CK """

from itertools import combinations

# Read input
input_str, k = input().split()
k = int(k)

# Generate combinations and print them
for i in range(1, k+1):
    # Generate combinations of length i
    comb = combinations(sorted(input_str), i)
    
    # Print each combination on separate lines
    for c in comb:
        print(''.join(c))
