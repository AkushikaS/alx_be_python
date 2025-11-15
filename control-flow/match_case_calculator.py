num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "-":
        result = float(num1) - float(num2)
        print(f"The result is {result}")
    case "+":
        result = float(num1) + float(num2)
        print(f"The result is {result}") 
    case "*":
        result = float(num1) * float(num2)
        print(f"The result is {result}")
    case "/":
        if float(num2) == 0:
            print("Error: Not Divisible")
        else:
            result = float(num1) / float(num2)
            print(f"The result is {result}")     


