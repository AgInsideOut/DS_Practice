""" Convert this function into a lambda:
    
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1] """


people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

# Original function
def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

# Lambda function
split_title_and_name_lambda = lambda person: person.split()[0] + ' ' + person.split()[-1]

# Option 1: Lambda function directly assigned to a variable
option_1 = lambda person: person.split()[0] + ' ' + person.split()[-1]

# Comparison for Option 1
comp_option_1 = all(split_title_and_name(person) == option_1(person) for person in people)

# Option 2: Apply lambda function using map()
option_2 = list(map(split_title_and_name_lambda, people))

# Comparison for Option 2
comp_option_2 = all(split_title_and_name(person) == formatted_person for person, formatted_person in zip(people, option_2))


list_formatted = []
for person in people:
    formatted = option_1(person)
    list_formatted.append(formatted)
    
print(f"\nOption 1 Results: {list_formatted}")
print("Option 1 Comparison:", comp_option_1)

print("\nOption 2 Result:", option_2)
print("Option 2 Comparison:", comp_option_2)

