import random
picks = int(input('How many quick picks?'))
for i in range(0,picks):
    number = []
    your_number = []
    number_remain = 45
    for i in range(1, 46):
        number.append(i)
    for i in range(0, 6):
        index = random.randint(0, number_remain - 1)
        number_remain = number_remain - 1
        your_number.append(number[index])
        number.remove(number[index])

    print(sorted(your_number))

