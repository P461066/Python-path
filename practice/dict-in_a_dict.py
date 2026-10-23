bookkeeper = { 
    "Temo": {
        "age": 678,
        "nationality": "African"
    }
}

# Only one loop needed:
for name, details in bookkeeper.items():
    print(f'NAME: {name}')
    print(f"AGE: {details['age']}")
    print(f"NATIONALITY: {details['nationality']}")