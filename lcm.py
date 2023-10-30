def find_least_common_multiple(a, b):
    maximum = max(a, b)
    while True:
        if maximum % a == 0 and maximum % b == 0:
            return maximum
        maximum += 1

num1 = float(input("Please Enter the First Number: "))
num2 = float(input("Please Enter the Second Number: "))
LCM = find_least_common_multiple(num1, num2)
print(f"\nLeast Common Multiple of {num1} and {num2} = {LCM}")
