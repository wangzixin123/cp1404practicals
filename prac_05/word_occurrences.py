# Get input text from the user
text = input("Text:")

# Split the input text into a list of words
words = text.split(' ')

# Create a dictionary to store word frequencies
word_amount = {}

# Initialize a variable to track the maximum word length
maximum_length = 0

# Count the frequency of each word in the input
for word in words:
    if word in word_amount.keys():
        word_amount[word] += 1
    else:
        word_amount[word] = 1

# Find the maximum length among all words for formatting
for key in word_amount.keys():
    if len(key) > maximum_length:
        maximum_length = len(key)

# Print the word frequencies with formatted alignment
for key, value in word_amount.items():
    print(f"{key:{maximum_length}}: {value}")

