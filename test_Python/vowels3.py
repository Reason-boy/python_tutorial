vowels = ['a', 'e', 'i', 'o', 'u']
#在终端输入单词再次运行即可，input本质是提供一个输入入口
word = input('Provide a word to search for vowels:')
found = []
for letter in word:
    if letter in vowels:
        #found.append函数的一个固定用法
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
