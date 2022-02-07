nums = [1, 2, 3, 4]
#remove里面是要删除的值而不是索引值
nums.remove(3)

#pop里面是索引值而不是要删除的值
#需要注意的是索引值从0开始
#如果pop里面没有内容，则是删除最后一个值
nums.pop()
nums.pop(0)

#extend用于将 两个列表合并
#注意括号和中括号，不要漏掉，extend本质是添加列表，中括号是必要的
nums.extend([6, 7])

#insert可以在指定索引值前插入对象(可以加入字符串)
nums.insert(0, 20)

#注意一个格式：列表.方法（）
#格式：模块.函数（）

#如何复制列表？使用赋值操作符是错误的，这种方法会形成列表引用和共享，两个列表会共享
first = [1, 2, 3]
second = first
#应当用.copy方法
third = second.copy()

#如何使用列表切片，见P79
#booklist[ : : ]