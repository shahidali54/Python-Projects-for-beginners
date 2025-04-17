import random

print("Welcome to the Password Generator!")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+;:,.~"

number = int(input("Enter the number of passwords to generate: "))

password_length = int(input("Enter the number of characters: "))

print('\nYour Passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(password_length):
        passwords += random.choice(characters)

    print(passwords)
