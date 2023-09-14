# Import necessary classes from external modules
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

# Initialize variables to keep track of the bill and the current taxi
bill = 0
current_taxi = None

# Create a list of available taxis, including regular and silver service taxis
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

# Define a menu for user interaction
MENU = "q)uit, c)hoose taxi, d)rive"

# Display an initial message to start the program
print("Let's drive!")
print(MENU)

# Get user input for their choice (quit, choose taxi, or drive)
choice = input('>>>').lower()

# Start a loop for user interaction
while choice != 'q':
    # If the user chooses to select a taxi
    if choice == 'c':
        taxi_number = 0
        print("Taxis available:")

        # Display a list of available taxis
        for taxi in taxis:
            print(f"{taxi_number} - {taxi}")
            taxi_number += 1

        # Prompt the user to choose a taxi
        taxi_choice = int(input('Choose taxi:'))

        # Check if the chosen taxi is within the valid range
        if taxi_choice > taxi_number - 1 or taxi_choice < 0:
            print('Invalid taxi choice')
        else:
            # Set the current taxi to the selected taxi
            current_taxi = taxis[taxi_choice]
    # If the user chooses to drive
    elif choice == "d":
        # Check if a taxi has been chosen
        if current_taxi is None:
            print('You need to choose a taxi before you can drive')
        else:
            # Prompt the user for the distance driven
            distance = int(input('Drive how far?'))

            # Simulate the taxi's trip and calculate the cost
            current_taxi.drive(distance)
            print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
            bill += current_taxi.get_fare()
    else:
        # Display an error message for an invalid option
        print("Invalid option")

    # Display the total bill to date
    print(f"Bill to date: ${bill:.2f}")
    print(MENU)

    # Prompt the user for their choice again
    choice = input('>>>').lower()
