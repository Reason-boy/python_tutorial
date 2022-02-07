vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels:")

found = {}

for letter in word:
    if letter in vowels:
        found[letter] += 1
        #错误出在上方的found后面没加上[letter]

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).' )