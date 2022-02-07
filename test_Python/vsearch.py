def search4vowels(word):
    """Display any vowels found in an asked-for word."""
    #多行注释简要描述函数的用途，通常用三引号
    vowels = set("aeiou")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
#当前终端什么都没有显示，说明还没有调用函数，上面为这个函数增加一个docstring（多行注释）