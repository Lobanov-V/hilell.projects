import string

text_for_hashtag = input("Enter your text: ")

words = text_for_hashtag.split()
words_capitalized = [word.capitalize().strip(string.punctuation) for word in words]


hashtag = '#' + ''.join(words_capitalized)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

# print(hashtag)