
number = int(input("Enter a number: "))

start = 1
end = 10

print(f"Multiplication Table for {number}:")

for i in range(start, end + 1):
    result = number * i
    print(f"{number} x {i} = {result}")
