# Travel Tracker 1.0 - Main Program
# Author: Zixin Wang

# This program serves as a travel tracker that helps users manage their travel destinations.
# Users can list places, get random recommendations, add new places, mark places as visited,
# and save their travel data to a CSV file.

import random

# Define the menu with options for the user.
MENU = """Menu:
    L - List places
    R - Recommend random place
    A - Add new place
    M - Mark a place as visited
    Q - Quit"""


# Main function that orchestrates the travel tracker functionality.
def main():
    # Initialize variables and load data from CSV file.
    filename = "places.csv"
    none_visited_places = []
    visited_places = []
    places = load_places(filename)

    # Separate places into visited and non-visited lists.
    for line in places:
        if line[3] == 'n':
            none_visited_places.append(line)
        else:
            visited_places.append(line)

    # Display program information and menu options.
    print('Travel Tracker 1.0 - by Zixin Wang')
    print(len(places), 'places loaded from', filename)
    print(MENU)
    choice = input('>>> ').lower()

    # Main program loop that processes user choices.
    while choice != 'q':
        if choice == 'l':
            list_places(none_visited_places, visited_places)
            print(f"{len(none_visited_places) + len(visited_places)} places. "
                  f"You still want to visit {len(none_visited_places)} places.")
        elif choice == 'r':
            if len(none_visited_places) == 0:
                print('No places left to visit!')
            else:
                place_number = random.randint(1, len(none_visited_places)) - 1
                print('Not sure where to visit next?')
                print(f"How about... {none_visited_places[place_number][0]} in {none_visited_places[place_number][1]}?")
        elif choice == 'a':
            city = get_nonempty_input('Name:')
            country = get_nonempty_input('Country:')
            priority = get_valid_priority()
            parts = [city, country, str(priority), 'n']
            none_visited_places.append(parts)
            print(f"{parts[0]} in {parts[1]} (priority {parts[2]}) added to Travel Tracker")
            none_visited_places = sort_places(none_visited_places)
        elif choice == 'm':
            list_places(none_visited_places, visited_places)
            if len(none_visited_places) == 0:
                print('No unvisited places')
            else:
                print(f"{len(none_visited_places) + len(visited_places)} places. "
                      f"You still want to visit {len(none_visited_places)} places.")
                print('Enter the number of a place to mark as visited')
                get_valid_place_number(none_visited_places, visited_places)
                none_visited_places = sort_places(none_visited_places)
                visited_places = sort_places(visited_places)
        else:
            print('Invalid menu choice')

        # Display menu again and get user's next choice.
        print(MENU)
        choice = input('>>> ').lower()

    # Save data back to the CSV file and display program exit message.
    save_places(filename, none_visited_places, visited_places)
    print(len(none_visited_places) + len(visited_places), 'places saved to', filename)
    print('Have a nice day :)')


# Function to list places, both visited and non-visited.
def list_places(none_visited_places, visited_places):
    places = none_visited_places + visited_places
    max_city_len = max(len(place[0]) for place in places)
    max_country_len = max(len(place[1]) for place in places)
    number = 0

    # Display each place's information.
    for line in none_visited_places:
        number += 1
        print(f"*{number}.{line[0]:{max_city_len}} in "
              f"{line[1]:{max_country_len}} {line[2]:>3}")
    for line in visited_places:
        number += 1
        print(f" {number}.{line[0]:{max_city_len}} in "
              f"{line[1]:{max_country_len}} {line[2]:>3}")


# Function to validate and process user's chosen place to mark as visited.
def get_valid_place_number(none_visited_places, visited_places):
    invalid_input = True
    while invalid_input:
        try:
            place_number = int(input('>>> '))
            if 0 < place_number <= len(none_visited_places) + len(visited_places):
                invalid_input = False
                if place_number <= len(none_visited_places):
                    print(f"{none_visited_places[place_number - 1][0]} in"
                          f" {none_visited_places[place_number - 1][1]} visited!")
                    none_visited_places[place_number - 1][3] = 'v'
                    visited_places.append(none_visited_places[place_number - 1])
                    none_visited_places.remove(none_visited_places[place_number - 1])
                    visited_places = sort_places(visited_places)
                else:
                    print(f"You have already visited"
                          f" {visited_places[place_number - 1 - len(none_visited_places)][0]}")
            elif place_number < 1:
                print('Number must be > 0')
            else:
                print('Invalid place number')
        except ValueError:
            print('Invalid input; enter a valid number')


# Function to load places from a CSV file.
def load_places(filename):
    places = []
    with open(filename, "r") as in_file:
        for line in in_file:
            if line.strip() != '':
                places.append(line.strip().split(','))
        in_file.close()
    return places


# Function to save places to a CSV file.
def save_places(filename, none_visited_places, visited_places):
    with open(filename, 'w') as out_file:
        for line in none_visited_places:
            out_file.write(','.join(line))
            out_file.write('\n')
        for line in visited_places:
            out_file.write(','.join(line))
            out_file.write('\n')
        out_file.close()


# Function to get a valid priority input from the user.
def get_valid_priority():
    invalid_input = True
    while invalid_input:
        try:
            priority = int(input('Priority:'))
            if priority <= 0:
                print('invalid input')
            else:
                invalid_input = False
                return priority
        except ValueError:
            print('Invalid input; enter a valid number')


# Function to get non-empty input from the user.
def get_nonempty_input(prompt):
    name = input(prompt)
    while name == '':
        print('Input cannot be blank')
        name = input(prompt)
    return name


# Function to sort places based on priority.
def sort_places(places):
    sorted_places = sorted(places, key=lambda place: int(place[2]))
    return sorted_places


# Call the main function to start the program.
main()
