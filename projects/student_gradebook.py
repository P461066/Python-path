student_gradebook = {}

def add_student():
    name = input("Enter student name: ").strip().capitalize()
    
    math = float(input("Enter Math grade: "))
    science = float(input("Enter Science grade: "))
    english = float(input("Enter English grade: "))
    python_code = float(input("Enter Python programming grade: "))
    
   
    student_gradebook[name] = {
        "math": math,
        "science": science,
        "english": english,
        "python_code": python_code
    }
    
    print(f"✅ Success! Added records for {name}.\n")


add_student()
add_student()


print("Full Gradebook Database:")
print( student_gradebook)


