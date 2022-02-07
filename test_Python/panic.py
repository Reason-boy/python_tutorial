phrase = "Don't panic!"
#list可以将字符串转化成为列表！
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")

#注意，这里plist.pop（）既是删除，又是返回对象，因此可以被extend和insert套用
# .pop()属于一个方法可以多个用途，本质相当于“删除并重置”的作用
plist.extend([plist.pop(), plist.pop()]) #在这行代码中，extend添加列表与for循环重复代码的作用相似
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)