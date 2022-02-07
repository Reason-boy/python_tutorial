fruits = {}
fruits['apples'] = 10

if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 1
#if函数本质是判断产生布尔值True和False，True则返回if下方，False则返回else下方。
print(fruits)

if 'pears' not in fruits:
    fruits['pears'] = 0
#用if/not in来简化上述if/else函数
fruits['pears'] += 1
print(fruits)

fruits.setdefault('pears', 0)
#用setdefault方法进一步简化上述代码，这个方法可以保证每次使用一个键之前，总有一个初始化的值，杜绝keyerror错误
fruits['pears'] += 1
print(fruits)