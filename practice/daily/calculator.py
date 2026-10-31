# ==========================================
# Running Total Calculator
# ==========================================
# Keeps adding numbers until you type 'done' (using a sentinel value loop)

total = 0.0
print("--- Running Total Calculator ---")
print("Enter numbers one by one. Type 'done' when you are finished.\n")

while True:
    user_input = input("Enter a number (or 'done'): ")
    
    # Sentinel value check to exit the loop
    if user_input.lower() == 'done':
        break
        
    try:
        # Convert user string input into a float so decimals work too
        number = float(user_input)
        total += number
        print(f"-> Current Total: {total}\n")
        
    except ValueError:
        # Handles bad input safely without crashing the script
        print("❌ Invalid input! Please enter a valid number or 'done'.\n")

print(f"\n==============================")
print(f"🏁 Final Total Sum: {total}")
print(f"==============================")