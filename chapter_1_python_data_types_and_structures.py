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