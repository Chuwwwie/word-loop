def loop_words(words, num_times):
    for _ in range(num_times):
        for word in words:
            print(word)

# Get user input for words
num_words = int(input("Enter the number of words: "))
words = []
for i in range(num_words):
    word = input("Enter word {}: ".format(i+1))
    words.append(word)

# Get user input for the number of times to loop
num_times = int(input("Enter the number of times to loop: "))

# Loop through the words
loop_words(words, num_times)
  
