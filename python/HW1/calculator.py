def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


print("Welcome to the Calculator Program!")
try:
    number_1 = int(input("Please enter the first number: "))
    number_2 = int(input("Please enter the second number: "))
except ValueError:
    print("You entered an invalid value, your value has to be a number. Try again")
    exit()

print("""
Please select an operation:
  1. Addition
  2. Subtraction
  3. Multiplication
  4. Division
""")
try:
    choice = int(input("Enter your choice (1-4): "))
except ValueError:
    print(f"You entered an invalid value, your value has to be number from 1 to 4. Try again")
    exit()

if choice == 1:
    result = addition(num1=number_1, num2=number_2)
    print(f"The result of addition is: {result}")

elif choice == 2:
    result = subtraction(num1=number_1, num2=number_2)
    print(f"The result of subtraction is: {result}")

elif choice == 3:
    result = multiplication(num1=number_1, num2=number_2)
    print(f"The result of multiplication is: {result}")

elif choice == 4 and number_2 != 0:
    result = division(num1=number_1, num2=number_2)
    print(f"The result of subtraction is: {result}")
elif number_2 == 0:
    print("Division by zero is undefined")

else:
    print(f"Your entered a wrong intput, please enter 1, 2, 3 or 4, your enter is {choice}")


