import random
import string


def generate_password(length):
    if length < 4:
        print("Password length must be at least 4.")
        return None

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lowercase + uppercase + digits + symbols

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)


def main():
    print("--- Strong Password Generator ---")

    try:
        count = int(input("How many passwords do you want to generate? "))
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if count <= 0:
        print("Number of passwords must be greater than 0.")
        return

    for i in range(count):
        password = generate_password(length)
        if password:
            print(f"Password {i + 1}: {password}")


main()
