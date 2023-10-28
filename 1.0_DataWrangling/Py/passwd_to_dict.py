""" 5 Files | Exercise 19 ■ /etc/passwd to dict
It's both common and useful to think of files as sequences of strings. After all, 
when you iterate over a file object, you get each of the file's lines as a string, 
one at a time. But it often makes more sense to turn a file into a more complex data 
structure, such as a dict.
In this exercise, write a function, passwd_to_dict, that reads from a Unix-style 
“password file,” commonly stored as /etc/passwd, and returns a dict based on it. 
If you don't have access tosuch a file, you can download one uploaded 
at http://mng.bz/2XXg.
Here's a sample of what the file looks like:
nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
Each line is one user record, divided into colon-separated fields. The first field 
(index 0) is the username, and the third field (index 2) is the user's unique ID 
number. (In the system from which I took the /etc/passwd file, nobody has ID -2, 
root has ID 0, and daemon has ID 1.) For our purposes, you can ignore all but these two fields.
Sometimes, the file will contain lines that fail to adhere to this format. For example, 
we generally ignore lines containing nothing but whitespace. Some vendors (e.g., Apple) 
include comments in their /etc/passwd files, in which the line starts with a # character.
The function passwd_to_dict should return a dict based on /etc/passwd in which the dict's 
keys are usernames and the values are the users' IDs.
Some help from string methods
The string methods str.startswith, str.endswith, and str.strip are helpful when doing this 
kind of analysis and manipulation.
For example, str.startswith returns True or False, depending on whether the string starts 
with a string:

s = 'abcd'
s.startswith('a')    # returns True
s.startswith('abc')  # returns True
s.startswith('b')    # returns False
Similarly, str.endswith tells us whether a string ends with a particular string:
s = 'abcd'
s.endswith('d')    # returns True
s.endswith('cd')   # returns True
s.endswith('b')    # returns False
str.strip removes the whitespace--the space character, as well as \n, \r, \t, and even \v--on either side of the string. The str.lstrip and str.rstrip methods only remove whitespace on the left and right, respectively. All of these methods return strings:
s = '   \t\t\ta  b  c  \t\t\n'
s.strip()    # returns 'a  b  c'
s.lstrip()   # returns 'a  b  c  \t\t\n'
s.rstrip()   # returns '   \t\t\ta  b  c' """

# SOLUTION 1
def passwd_to_dict(file_path):
    # Dictionary to store usernames as keys and user IDs as values
    user_dict = {}
    
    try:
        # Open the file and read lines
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            # Iterate through lines and extract username and user ID
            for line in lines:
                # Ignore lines starting with '#' (comments) and empty lines
                if line.strip() and not line.startswith('#'):
                    # Split the line by colon and extract username and user ID
                    fields = line.strip().split(':')
                    username = fields[0]
                    user_id = fields[2]
                    
                    # Update the dictionary with username as key and user ID as value
                    user_dict[username] = int(user_id)
    
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    
    return user_dict

# # SOLUTION 2 :
# def passwd_to_dict(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             # Read lines, filter out comments and empty lines, extract username and user ID
#             lines = filter(lambda x: x.strip() and not x.startswith('#'), file.readlines())
#             # Form a dictionary through lambda function, extract username and user ID
#             user_dict = dict(map(lambda x: (x.strip().split(':')[0], int(x.strip().split(':')[2])), lines))
#         return user_dict
#     except FileNotFoundError:
#         print(f"Error: File not found at {file_path}")


#CALL A FUNCTION
# Example usage
file_path = "path/to/your/etc/passwd/file"  # Replace this with the actual file path
users = passwd_to_dict(file_path)
print(users)
