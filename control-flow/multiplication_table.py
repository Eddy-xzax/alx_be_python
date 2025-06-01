number = int(input("Enter a number to see its multiplication table: "))
x = number
for Y in range(1, 11):
    Z = x * Y
    print(f"{number} * {Y} = {Z}")
