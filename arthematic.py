# input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# perform arithmetic operations
add = num1 + num2 # addition
sub = num1 - num2 # subtraction
mul = num1 * num2 # multiplication
div = num1 / num2 # division
mod = num1 % num2 # modulus
exp = num1 ** num2 # exponentiation
flo = num1 // num2 # floor division

# display the results
print("The sum of", num1, "and", num2, "is", add)
print("The difference of", num1, "and", num2, "is", sub)
print("The product of", num1, "and", num2, "is", mul)
print("The quotient of", num1, "and", num2, "is", div)
print("The remainder of", num1, "divided by", num2, "is", mod)
print("The result of", num1, "raised to the power of", num2, "is", exp)
print("The result of", num1, "floor divided by", num2, "is", flo)