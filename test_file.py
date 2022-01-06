text = "Abc"
text = list(text)[::-1]
for i in text:
    if i.islower():
        print(i.capitalize())
    if i.isupper():
        print(i.lower())
