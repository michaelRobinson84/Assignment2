word_occurences_dict = {}

string_to_analyze = input("Enter a string to analyze: ")

for word in string_to_analyze.split(" "):
    if word in word_occurences_dict:
        word_occurences_dict[word] = word_occurences_dict[word] + 1
    else:
        word_occurences_dict[word] = 1

dictionary_items = word_occurences_dict.items()
sorted_items = sorted(dictionary_items)

longest_length = 0
dict_keys = word_occurences_dict.keys()

for key in dict_keys:
    if len(key) > longest_length:
        longest_length = len(key)

for key, value in sorted_items:
     print("{:{}}:".format(key, longest_length), end=' ')
     print(value)