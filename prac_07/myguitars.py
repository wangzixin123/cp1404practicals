from prac_07.guitar import Guitar

filename = 'guitars.csv'
guitars = []
with open(filename, "r") as in_file:
    for line in in_file:
        if line != '':
            parts = line.strip().split(',')
            # print(parts)
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
in_file.close()
for guitar in guitars:
    guitars.sort()
    print(guitar)



