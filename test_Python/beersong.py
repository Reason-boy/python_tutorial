WORD = "bottles"
#注意学习倒数循环函数,range中最后的值不参与循环
for beer_number in range(99, 0, -1):
    print(beer_number, WORD, "of beers on the wall.")
    print(beer_number, WORD, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    #一个print写一行，if和else做选择，本质是描述条件
    if beer_number == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_number = beer_number - 1
        #if本质是描述条件，添加条件
        if new_number == 1:
            WORD = "bottle"
        print(new_number, WORD, "of beer on the wall.")
    print()

#算法和伪代码之间是一一对应的，在这个练习中，对应体现的是文本逐句对应。
#通过对比去掉某行代码理解原有代码的用意