# Start with our main empty dictionary 
student_gradebook = {}

def add_student():
    # 1. Get the student's name as a string (Day 1 & 5 notes)
    name = input("Enter student name: ").strip().capitalize()
    
    # 2. Get grades for multiple subjects and convert them to floats or ints 
    # (Day 2 & 5 notes: Arithmetic & Type Conversion)
    math = float(input("Enter Math grade: "))
    science = float(input("Enter Science grade: "))
    english = float(input("Enter English grade: "))
    python_code = float(input("Enter Python programming grade: "))
    
    # 3. Store everything in a larger nested dictionary structure (Day 22 notes)
    student_gradebook[name] = {
        "math": math,
        "science": science,
        "english": english,
        "python_code": python_code
    }
    
    print(f"✅ Success! Added records for {name}.\n")

# Test running it twice to add a couple of students!
add_student()
add_student()

# Print the full dictionary to see how it looks
print("Full Gradebook Database:")
print( student_gradebook)# Start with our main empty dictionary (Day 22 notes)


