for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
numbers_of_stars = int(input('Number of stars:'))
for i in range(0, numbers_of_stars):
    print('*', end=' ')
print()
numbers_of_stars = int(input('Number of stars:'))
for i in range(0, numbers_of_stars):
    for j in range(0, i+1):
        print('*', end=' ')
    print()

