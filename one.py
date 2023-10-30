# Program to swap two numbers and check the sign

# Input two numbers from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Display the original values of a and b
print('Before swap:')
print('a =', a)
print('b =', b)

# Swap the values of a and b using a temporary variable 'temp'
temp = a
a = b
b = temp

# Display the swapped values of a and b
print('\nAfter swap:')
print('a =', a)
print('b =', b)

# Check the sign of the first number (a) and print the result
if a > 0:
    print('\nThe first number after swap is positive')
elif a < 0:
    print('\nThe first number after swap is negative')
else:
    print('\nThe first number after swap is zero')
