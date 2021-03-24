test_string = "This isn't not good"
print(test_string)
test_string = 'This "is" good too!'
print(test_string)
test_string = """this is
a test
today"""
print(test_string)

test_string = "12345"
reverse_string = test_string[::-1]
print(reverse_string)

for char in "hi mum":
    print(char, type(char))

word = 'spam'

new_word = word[:1] + 'l' + word[2:]

print(new_word)

print (new_word[0:1])


