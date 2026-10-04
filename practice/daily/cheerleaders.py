an_letters = "aefhilmnorsxAEFHILMNORSX "
word = input("I will cheer for you! Enter a word: ")
times = int(input("On a scale of 1 to 10, how much do you want me to cheer for you? "))


for letter in word:
        if letter in an_letters:
            print("Give me an  " + letter + "!  " + letter)
        else:
            print("Give me a  " + letter + "!  " + letter)

print("What does that spell?")
for i in range(times):
    print(word + "! ", end="")