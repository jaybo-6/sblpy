import os

def menu():
    print("\n///MENU///")
    print("1. To count the number of lines, words, and characters in a file")
    print("2. To display files in the current directory")
    print("3. Exit")
    return int(input("\nEnter your choice: "))

c = 0
while c != 3:
    c = menu()
    if c == 1:
        c = l = w = 0
        fname = input("\nEnter the file name: ")
        with open(fname + ".txt", "r") as f:
            for x in f:
                words = x.split()
                l += 1
                w += len(words)
                c += len(x)
        print("\nNo. of lines =", l)
        print("No. of words =", w)
        print("No. of characters =", c)
    elif c == 2:
        print("\nThe files in the current directory are:\n")
        for subdir, dirs, files in os.walk('./'):
            for file in files:
                print(file)
    elif c != 3:
        print("\nIncorrect choice")
