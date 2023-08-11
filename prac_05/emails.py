# Initialize an empty dictionary to store name-to-email mappings
name_to_email = {}

# Start a loop to collect email and name information from the user
email = input('Email:')

while email != '':
    # Extract the name from the email address
    name = email.split('@')[0]

    # Split the name by periods and capitalize each part
    parts = [part for part in name.split('.')]
    name = " ".join(parts).title()

    # Ask the user if the derived name is correct
    choice = input(f"Is your name {name}? (Y/n) ").lower()

    # Store the name and email in the dictionary based on user input
    if choice == '' or choice == 'y':
        name_to_email[name] = email
    else:
        name = input("Name: ")
        name_to_email[name] = email

    # Prompt the user for another email
    email = input('Email:')

# Print the collected name-to-email mappings
for name, email in name_to_email.items():
    print(f"{name} ({email})")
