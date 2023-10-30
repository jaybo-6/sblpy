# Initialize empty lists
l = []
l1 = []
l2 = []

# Function to display the menu and return the user's choice
def menu():
    print("\nMENU")
    print("1. Even & Odd")
    print("2. Merge & Sort")
    print("3. Update & Delete")
    print("4. Min & Max")
    print("5. Add names into list")
    print("6. Exit")
    return int(input("\nEnter your choice: "))

# Function to separate even and odd numbers
def evenodd():
    for i in l:
        if i % 2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    print("\nEven numbers are: ")
    print(l1)
    print("\nOdd numbers are: ")
    print(l2)

# Function to merge, sort, and display the list
def merge():
    l3 = l1 + l2
    print("\nThe merged list is:\n", l3)
    l3.sort()
    print("\nSorting in ascending order:\n", l3)
    print("\nSorting in descending order:\n", l3[::-1])

# Function to update the first element and delete the middle element
def update():
    x = int(input("\nEnter the element to be placed in the first position: "))
    l[0] = x
    print("\nThe updated list is:\n", l)

    n = len(l)
    if n % 2 == 0:
        l.pop(n // 2 - 1)
    else:
        l.pop(n // 2)
    print("\nAfter deleting the middle element, the list is:\n", l)

# Function to find the minimum and maximum elements in the list
def minmax():
    print("\nThe minimum element of the list is:", min(l))
    print("\nThe maximum element of the list is:", max(l))

# Function to add names to the list and check for the presence of 'python'
def add():
    n1 = int(input("\nEnter the number of strings to store in the list: "))
    print("\nEnter the strings:")
    for i in range(0, n1):
        s = input()
        l.append(s)
    print("\nThe updated list is:\n", l)
    if 'python' in l:
        print("\nThe string 'python' is present in the list")
    else:
        print("\nThe string 'python' is not present in the list")

# Read the number of elements for the initial list
n = int(input("\nEnter the number of elements to store in the list: "))
print("\nEnter the list numbers:")
l = [int(x) for x in input().split()]
print("\nThe list is:\n", l)

c = 0
while c != 6:
    c = menu()
    if c == 1:
        evenodd()
    elif c == 2:
        merge()
    elif c == 3:
        update()
    elif c == 4:
        minmax()
    elif c == 5:
        add()
    elif c != 6:
        print("\nIncorrect choice")
