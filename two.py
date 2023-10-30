# Function to display the menu and return the user's choice
def menu():
    print("\nMENU")
    print("1. Palindrome")
    print("2. Factorial")
    print("3. Pattern")
    print("4. Exit")
    return int(input("\nEnter your choice: "))

# Function to check if a string is a palindrome
def palindrome():
    flag = 1
    string = input("\nEnter the string: ")
    for i in range(0, len(string) // 2): 
        if string[i] != string[len(string) - i - 1]:
            flag = 0
            break
    if flag == 1:
        print("\nThe string is a palindrome")
    else:
        print("\nThe string is not a palindrome")

# Function to calculate the factorial of a number
def fact():
    f = 1
    n = int(input("\nEnter the number: "))
    for i in range(2, n + 1):
        f = i * f
    print("\nThe factorial =", f)

# Function to print a pattern of stars
def pattern():
    n = int(input("\nEnter the number of rows: "))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

choice = 0
while choice != 4:
    choice = menu()
    if choice == 1:
        palindrome()
    elif choice == 2:
        fact()
    elif choice == 3:
        pattern()
