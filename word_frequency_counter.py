import string
s = input("Enter a string: ")
s = s.lower()
s = s.translate(str.maketrans('', '', string.punctuation))
words = s.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("Word Frequency:")
print(frequency)