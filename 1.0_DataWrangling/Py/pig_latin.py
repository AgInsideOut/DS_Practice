""" Pig Latin (http://mng.bz/YrON) is a common children's "secret" language in English-speaking countries. 
(It's normally secret among children who forget that their parents were once children themselves.) 
The rules for translating words from English into Pig Latin are quite simple:
If the word begins with a vowel (a, e, i, o, or u), add "way" to the end of the word. So "air" becomes 
"airway" and "eat" becomes "eatway."
If the word begins with any other letter, then we take the first letter, put it on the end of the word, 
and then add "ay." Thus, "python" becomes "ythonpay" and "computer" becomes "omputercay."
(And yes, I recognize that the rules can be made more sophisticated. Let's keep it simple for the 
purposes of this exercise.)
For this exercise, write a Python function (pig_latin) that takes a string as input, assumed to be an 
English word. The function should return the translation of this word into Pig Latin. You may assume 
that the word contains no capital letters or punctuation.
This exercise isn't meant to help you translate documents into Pig Latin for your job. (If that is your 
job, then I really have to question your career choices.) However, it demonstrates some of the powerful 
techniques that you should know when working with sequences, including searches, iteration, and slices. 
It's hard to imagine a Python program that doesn't include any of these techniques. """

# Initialize a string

def pig_latin(word):
    # If the word begins with a vowel (a, e, i, o, or u), add "way" to the end of the word.
    if word[0] in "aeiou":
        word = word + "way"
    # If the word begins with any other letter
    else:
        word = word[1:] + word[0] + "ay"
    return word

# Test the function
word = "python"
pig_latin_translation = pig_latin(word)
print(pig_latin_translation)



