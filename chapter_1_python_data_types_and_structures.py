# """Kysymys 1
#  Write a program that takes a single string as its input
#  and sort its characters from the lowest Unicode value to 
# the highest Unicode value. The program should print the new
#  string. """
input_string = input()

#sort the characnters of the input string
sorted_string = ''.join(sorted(input_string))

#print the sorted string
print(sorted_string)

""" Kysymys 2
Write a program that takes two integers, a and b, as input.
Your program should compute and display:
The sum of a and b
The difference when b is subtracted from a
The product of a and b
The quotient when a is divided by b
The remainder when a is divided by b
The result of  """

a = int(input())
b = int(input())

# Perform arithmetic operations
sum_ab = a + b
difference_ab = a - b
product_ab = a * b
quotient_ab = a / b
remainder_ab = a % b
exponent_ab = a ** b

# Display the results
print(f"{a} + {b} is {sum_ab}")
print(f"{a} - {b} is {difference_ab}")
print(f"{a} * {b} is {product_ab}")
print(f"{a} / {b} is {quotient_ab}")
print(f"{a} % {b} is {remainder_ab}")
print(f"{a} ^ {b} is {exponent_ab}")

""" Kysymys 3
Write a program that prints a dictionary where the keys are numbers between 1 and N, 
and the values are square of keys.

Input Specification: The first line of input contains N
Output Specification: Print the dictionary """

N = int(input())

squares = {i: i **2 for i in range(1, N+1)}

print(squares)

""" Kysymys 4
Sum of the First n Positive Integers
Write a program that takes a positive integer, n, as input and then 
displays the sum of all of the integers from 1 to n. The sum of the
 first n positive integers can be computed using the formula:
 sum = n * (n+1)/2 """
# Read n from the user
n = int(input())

# Calculate the sum using the formula
sum_n = n * (n + 1) // 2

# Print the result
print(f"The sum of the first {n} positive integers is {sum_n}")

""" Kysymys 5
Count vowels
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in 
the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

For example, if s = 'hello', your program should print:

Number of vowels: 2 """

def count_vowels(s):
    # Convert s to lowercase to ensure case-insensitive counting
    s = s.lower()
    # Define the vowels
    vowels = 'aeiou'
    # Count and sum up the vowels in the string s
    vowel_count = sum(1 for char in s if char in vowels)
    # OR:
    # sum = 0
    # for char in s:
    #     if char in vowels:
    #         sum +=1
    return vowel_count

# Read input string from standard input (e.g., Moodle test environment)
s = input()

# Output the number of vowels
print(f"Number of vowels: {count_vowels(s)}")

# Kysymys 6
""" Write a program that sums all of the numbers taken as input,
 while ignoring any input that is not a valid number.
Your program should display the current sum after each Number
 is entered. It should display an error message after each 
 non-numeric input, and then continue to sum any additional 
 numbers entered by the user.  The program exits when the user
  enters 0. 
Ensure that your program works correctly for both integers 
and floating-point numbers. """

total = 0.0

while True:
    user_input = input()
    if user_input == "0":
        print(f"The grand total is {total}")
        break
    try:
        number = float(user_input)
        total += number
        print(f"The total is now {total}")
    except ValueError:
        print("That wasn’t a number.")

# Kysymys 7
""" Custom encoder
Write a function called "custom_encoder" that accepts a string text 
as parameter and for each char of the text it calculates its 
0-based position in the following reference string:

reference_string = 'abcdefghijklmnopqrstuvwxyz' """

def custom_encoder(text):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    positions = []
    for char in text.lower():  # Convert to lowercase to match the reference string
        if char in reference_string:
            positions.append(reference_string.index(char))
        else:
            positions.append(-1)
    return positions

# Kysymys 8
""" Write a class Person that has a member function hello()
The output from your program, when called with the code 
in the Test column, should be exactly as shown in the Result column: """

class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
       print(f"Hello, my name is {self.name}")

# Kysymys 9
""" Restaurant
Make a class called Restaurant. The __init__() method for Restaurant 
should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two 
pieces of information, and a method called open_restaurant() that
 prints a message indicating that the restaurant is open. """

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")

