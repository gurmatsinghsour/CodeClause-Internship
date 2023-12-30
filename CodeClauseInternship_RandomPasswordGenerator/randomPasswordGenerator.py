import random

def generate_password(length):
    characters = {
        'capital_letters': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        'small_letters': "abcdefghijklmnopqrstuvwxyz",
        'digits': "0123456789",
        'punctuations': "~!@#$%^&*()_+=-|/.,><?;':"
    }

    password = (
        random.choice(characters['capital_letters']) +
        random.choice(characters['small_letters']) +
        random.choice(characters['digits']) +
        random.choice(characters['punctuations'])
    )

    for _ in range(4, length):
        password += random.choice(
            characters['capital_letters'] +
            characters['small_letters'] +
            characters['digits'] +
            characters['punctuations']
        )

    shuffled_password = ''.join(random.sample(password, len(password)))
    return shuffled_password

def main():
    number_of_passwords = int(input("Enter the number of passwords required: "))
    password_length = max(4, int(input('Enter the password length (min 4): ')))

    for j in range(number_of_passwords):
        password = generate_password(password_length)
        print(f"Password {j + 1}: {password}")

if __name__ == "__main__":
    main()
