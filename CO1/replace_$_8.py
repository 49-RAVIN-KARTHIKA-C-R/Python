word=input("Enter the word:")
first=word[0]
word=word.replace(first,"$")
word=first+word[1:]
print(word)