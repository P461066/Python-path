def check_resistor_power(voltage, resistance, max_power_rating):
    # Step 1: Calculate power dissipation using P = V^2 / R
    power_dissipated = (voltage ** 2) / resistance
    
    # Step 2: Check if the component can handle the load
    if power_dissipated <= max_power_rating:
        status = "Safe"
    else:
        status = "At Risk of Burning Out!"
        
    # Step 3: Return a formatted status message (rounded to 2 decimal places)
    return f"Dissipated Power: {power_dissipated:.2f}W | Status: {status}"

# Test it with some numbers (e.g., 12V across a 100-ohm resistor with a 0.5W rating)
result = check_resistor_power(12, 100, 0.5)
print(result)