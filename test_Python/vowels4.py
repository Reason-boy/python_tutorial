vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels:")

found = {}

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
#以上属于初始化代码，将各个元音的频度计数初始设置为0
#没有初始化的键是不存在的

for letter in word:
    if letter in vowels:
        found[letter] += 1
        #错误出在上方的found后面没加上[letter]

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).' )