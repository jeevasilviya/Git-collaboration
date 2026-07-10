from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from division import division

while True:

    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice == "5":
        print("Thank You!")
        break

    if choice not in ["1","2","3","4"]:
        print("Invalid Choice")
        continue

    num1 = float(input("Enter First Number : "))
    num2 = float(input("Enter Second Number : "))

    if choice == "1":
        print("Result =", addition(num1, num2))

    elif choice == "2":
        print("Result =", subtraction(num1, num2))

    elif choice == "3":
        print("Result =", multiplication(num1, num2))

    elif choice == "4":
        print("Result =", division(num1, num2))