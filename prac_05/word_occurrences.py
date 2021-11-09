
user_words = input("Please enter your statement: ")  # Step 1
print(user_words)  # Step 1
count_of_words = dict()  # Step 2 - Convert to Dictionary
words = user_words.split()  # Step 3 - Splitting string into 'words', storing in 'words'

for every_word in words:  # Step 4 - Count the frequency of words in "words"
    if every_word in count_of_words:
        count_of_words[every_word] += 1  # If the words is coming twice, iterate
    else:
        count_of_words[every_word] = 1
data_of_words = []  # Step 5 - declare empty list to store 2 things - Words - & their respective frequencies
for word_name, word_frequency in count_of_words.items():
    data_of_words.append(word_name)
longest_word_in_data_of_words = max(data_of_words, key=len)
index_num_word = data_of_words.index(longest_word_in_data_of_words)
for word_name, word_frequency in count_of_words.items():
    print("{:{}} = {}".format(word_name, len(longest_word_in_data_of_words), word_frequency))
