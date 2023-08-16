import random
import string

up_letters = string.ascii_uppercase
low_letters = string.ascii_lowercase
digits = string.digits
spec_symbols = string.punctuation

print("Welcome to the Linux User Password Generator!")
try:
    length = int(input("Please enter the desired password length: "))
    if length <= 4:
        print("Length should be at least 4.")
        exit()

    password = (
            random.choice(up_letters)
            + random.choice(low_letters)
            + random.choice(digits)
            + random.choice(spec_symbols)
            + ''.join(random.choice(up_letters + low_letters + digits + spec_symbols) for _ in range(length - 4))
    )
    print(password)
except ValueError:
    print(f"You should enter numeric value")
