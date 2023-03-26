def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "Y"
            else:
                translation += "y"
        else:
            translation += letter
    return translation


print(translate(input("Enter a phrase: ")))

