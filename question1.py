"""

    ASSIGNMENT #
    QUESTION 1
    AUTHOR: Bonnie Ives de Castro Nunes
    DATE: September 15th, 2023
    
"""

print("Please inform the first number: ")
firstNumber = input()
print("-------------------------------")

print("Please inform the second number: ")
secondNumber = input()
print("-------------------------------")

print("First number informed: " + firstNumber)
print("Second number informed: " + secondNumber)
print("-------------------------------")

product = int(firstNumber) * int(secondNumber)

if int(product) > 1000:
    summing = int(firstNumber) + int(secondNumber)
    print("The sum between " + str(firstNumber) + " and " + str(secondNumber) + " is " + str(summing))
else:
    print("The product between " + str(firstNumber) + " and " + str(secondNumber) + " is " + str(product))
