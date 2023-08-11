def main():
    print("""C : Convert Celsius to Fahrenheit
F : Convert Fahrenheit to Celsius""")
    choice = input('choice:').lower()
    if choice == "c":
        celsius = float(input("Celsius: "))
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "f":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid choice")


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()
