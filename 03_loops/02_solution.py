# n = 10
n = int(input("Enter the number of elements: "))

sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers is : ",sum_even )