import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Define the possible character sets
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # Adds both lowercase and uppercase letters
    if use_numbers:
        characters += string.digits  # Adds digits 0-9
    if use_symbols:
        characters += string.punctuation  # Adds symbols like !, @, #

    # Ensure there's at least one character set selected
    if not characters:
        print("Error: No character sets selected. Please enable at least one of letters, numbers, or symbols.")
        return None

    # Generate the password using random choice from the selected character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    # Get password length from user
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Password length must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer for password length.")

    # Get character set preferences from the user
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    return length, use_letters, use_numbers, use_symbols

def main():
    print("Welcome to the Password Generator!")
    length, use_letters, use_numbers, use_symbols = get_user_input()
    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
