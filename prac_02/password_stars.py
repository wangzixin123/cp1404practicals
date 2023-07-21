MINIMUM_LENGTH = 4


def main():
    """Get and print password using functions."""
    password = get_password(MINIMUM_LENGTH)
    print('*' * len(password))


def get_password(minimum_length):
    """Get password, ensuring it meets the minimum_length requirement."""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("invalid password length")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


main()

