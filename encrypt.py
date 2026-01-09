import string
import random

chars = string.punctuation + string.digits + string.ascii_letters + string.whitespace

chars = list(chars)
key = chars.copy()

random.shuffle(key)


encrypt_text = input("Enter the text: ")

encrypted = ""


if encrypt_text:
    for letter in encrypt_text:
        if letter in chars:
            index = chars.index(letter)
            encrypted += key[index]
else:
    print("You must be input encrypt_text!")
print(encrypted)

print("Do you want convert encypted to encrypt? (Y/N)")
choice = input("Enter your choice: ").lower()
convert = ""
if choice == "y":
    for letter in encrypted:
        if letter in key:
            index = key.index(letter)
            convert += chars[index]
    print(f"Text convert is: {convert}")
