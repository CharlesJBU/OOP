number1 = int(input("insert value:"))
number2 = int(input("insert value:"))
operator = input("+,-,*,/:")

if operator == "+":
    print("The sum is:", number1 + number2)
elif operator == "-":
    print("The sum is:", number1 - number2)
elif operator == "*":
    print("The sum is:", number1 * number2)
else:
    print("the sum is:", number1 / number2)