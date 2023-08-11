# Define the filename of the CSV dataset
filename = "wimbledon.csv"

# Define the indices of columns in the CSV
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

# Initialize lists and dictionaries to store data
records = []  # To hold all CSV records
champion_to_count = {}  # To count champion occurrences
countries = set()  # To store unique countries

# Read and process the CSV file
with open(filename, "r", encoding="utf-8-sig") as in_file:
    in_file.readline()  # Skip the header line
    for line in in_file:
        parts = line.strip().split(",")
        records.append(parts)

# Count champion occurrences and collect countries
for record in records:
    countries.add(record[INDEX_COUNTRY])
    try:
        champion_to_count[record[INDEX_CHAMPION]] += 1
    except KeyError:
        champion_to_count[record[INDEX_CHAMPION]] = 1

# Display Wimbledon champion information
print("Wimbledon Champions:")
for name, count in champion_to_count.items():
    print(name, count)

# Display countries that have won Wimbledon
print(f"\nThese {len(countries)} countries have won Wimbledon:")
print(", ".join(country for country in sorted(countries)))
