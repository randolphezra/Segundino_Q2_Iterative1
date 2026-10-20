def getSum(limit):
    sum = 0
    for i in range(limit + 1):
        sum += i
    return sum
n = int(input("Hi there! Please enter your age: "))
while (n <= 0):
        n = int(input("Please enter a whole number greater than 0. " \
        "Hi there! Please enter your age: "))
total = getSum(n)
s = n * (n + 1) // 2
if total == s:
    print(f"Output verified. The sum of all numbers from 1 to {n} is: {total}.")
else:
    print(f"Output not verified. The sum of all numbers from 1 to {n} is: {total}.")