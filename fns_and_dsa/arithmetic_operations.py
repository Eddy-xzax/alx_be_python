def perform_operation(num1, num2, operation):
 #prompts the user to insert a number
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = (input('add','subtract','multiply','divide'))
    
    if operation == ('add'):
       return num1 + num2
    elif operation == ('subtract'):
        return num1 - num2
    elif operation == ('multiply'):
        return num1 * num2
    elif operation == ('divide'):
        if num2 == 0:
           return "Error: cannot be divided by zero"
        return num1 / num2   
    else:
        return "Unknown operation"
