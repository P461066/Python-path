def mult_add(a, b):
    result = 0 
    while b > 0:
        result += a
        b -= 1
    return result
final_result = mult_add(6, 4)
print(final_result)