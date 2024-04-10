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