while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        op = input("Enter the operator (+,-,*,/): ")

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Error: division by zero")
                continue
            result = num1 / num2
        else:
            print("Error: invalid operator")
            continue

        print(f"{num1} {op} {num2} = {result}")
    except ValueError:
        print("Error: invalid input")
    
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != "y":
        break
