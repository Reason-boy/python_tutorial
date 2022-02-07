#模块可以看成是相关函数的集合
from datetime import datetime
odds = [ 1,  3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 57, 59 ]
for i in range(5):  
    right_this_time= datetime.today().minute

    #in是python中一个非常强大的操作符，可以判断一个对象是否在另一个对象中
    #if语句的结果为“True”或者“False”

    #如果有多个需要检查的条件要作为if语句的一部分，用elif
    #例子：
    #if today == “Saturday”:
    #   print("Party!")
    #elif today == "Sunday":
    #   print("Recover.")
    #else:
    #   print("Work, work, work.")                                                                                                                                                                                                           
    if right_this_time in odds:

        #python中的块/代码组非常容易判断，因为它们总是以缩进的形式出现，上方通常有冒号（：）提示
        #冒号（：）引入一个必须缩进的代码组，通常如果没有缩进，解释器会报错
        print("This minute seems a little odd.")

    #通常，当if语句返回一个False值时会执行else的代码组
    #else语句需要取消缩进与if对齐
    else:
        print("Not an odd minute.")




#拓展这个程序
#使用python shell进行试验代码段，它是REPL（read-eval-print-loop），在拓展基础程序编写的时候通常用来试验（哎，好像有点难）