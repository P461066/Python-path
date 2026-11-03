  # Check if a number is even or odd
# Step 1: Ask the user for a number (only integers)
num = int(input("Enter a number: "))

# Step 2: Check if the number is divisible by 2
if num % 2 == 0:
    # Step 3: Print the even message
    print(f"{num} is even")
else:
    # Step 3: Print the odd message
    print(f"{num} is odd")
