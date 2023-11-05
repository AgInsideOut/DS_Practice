""" Here, why don’t you try converting a function into a list comprehension. :
    def times_tables():
        lst = []
        for i in range(10):
            for j in range (10):
                lst.append(i*j)
        return lst """
        
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [i * j for i in range(10) for j in range(10)]

result = times_tables()
print(result)

# -------

""" Many organizations have user ids which are constrained in some way. Imagine you work at an internet service 
provider and the user ids are all two letters followed by two numbers (e.g. aa49). Your task at such an 
organization might be to hold a record on the billing activity for each possible user. 

Write an initialization line as a single list comprehension which creates a list of all possible user ids. 
Assume the letters are all lower case.

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [???]
correct_answer == answer """

# First option

import itertools

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

# Generate all possible combinations of two letters followed by two digits
user_ids = [''.join(combination) for combination in itertools.product(lowercase, repeat=2)]
user_ids = [user_id + str(number) for user_id in user_ids for number in range(10)]

# Print the user_ids to see the result
print(user_ids)

# Calculate the number of combinations
num_combinations = len(user_ids)
print("Number of combinations:", num_combinations)

# Store the correct answer for comparison
correct_answer = user_ids[:]


# Second option

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

print(correct_answer[:50]) # Display first 50 ids
