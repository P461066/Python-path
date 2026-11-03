def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Can't divide by zero gang!"
    return a / b

# Daily practice loop
while True:
    print("\n--- Pablo's Calc ---")
    print("1:Add 2:Sub 3:Mul 4:Div 5:Exit")
    
    choice = input("Pick: ")
    
    if choice == '5':
        print("Shutting down, boss.")
        break
    
    if choice not in ['1','2','3','4']:
        print("Invalid, try again")
        continue

    try:
        x = float(input("First number: "))
        y = float(input("Second number: "))
    except:
        print("Yo, numbers only!")
        continue

    if choice == '1':
        print(f"Result: {add(x,y)}")
    elif choice == '2':
        print(f"Result: {sub(x,y)}")
    elif choice == '3':
        print(f"Result: {mul(x,y)}")
    elif choice == '4':
        print(f"Result: {div(x,y)}")