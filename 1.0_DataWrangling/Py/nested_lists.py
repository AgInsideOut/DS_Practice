""" Given the names and grades for each student in a class of  students, store them in a 
nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names 
alphabetically and print each name on a new line.

Example :
The ordered list of scores is , so the second lowest score is . There are two students with 
that score: . Ordered alphabetically, the names are printed as:
alpha
beta

Input Format :
The first line contains an integer, , the number of students. 
The  subsequent lines describe each student over  lines. 
- The first line contains a student's name. 
- The second line contains their grade.

Constraints:
There will always be one or more students having the second lowest grade.
Output Format
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple 
students, order their names alphabetically and print each one on a new line.
Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0
Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so 
we order their names alphabetically and print each name on a new line. """

#   if __name__ == '__main__':                  #   Checks if the Python script is being run directly (not imported into another module)
#       for _ in range(int(input())):           #   Prompts the user for input (presumably an integer) and creates a loop that iterates the number of times specified by the user input. 
#                                               #   The loop variable _ is commonly used when the loop variable is not actually used in the loop body, as is the case here.

        
if __name__ == '__main__':
    students = []  # Create an empty list to save student names and grades.

    # Read the number of students input.
    n = int(input())

    # Read student names and grades and save them as sublists in the'students' list.
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade
    scores = set([student[1] for student in students])
    second_lowest_score = sorted(scores)[1]

    # Sort the names of students with the second lowest grade alphabetically.
    selected_students = sorted([student[0] for student in students if student[1] == second_lowest_score])

    # Print names of selected students
    for student in selected_students:
        print(student)
        
#   Regarding your use of __ in unittests, it's important to note that the double underscore (__) 
# has special meanings in Python, and its usage can vary depending on the context. In the context 
# of unittests, double underscores are often used to create special methods or attributes for test 
# cases, but it's not directly related to the __name__ variable used in the provided code.
