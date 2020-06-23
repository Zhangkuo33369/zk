#  ==判断是否相等   tab缩进4个空格   if else后面冒号而不是分号
#   =赋值    晚上神色吧要不台词眼睛了，白天在浅色好一点
"""
a = input("请输入：")
if a == "" :
    print("不能为空！")
    exit()
if a in "0123456789":
    a =int(a)
else:
    print("给老子重新输入！")
    exit()    #退出
if a>5 :
    print(牛逼)
else:
    print(弟弟)    
"""
"""
a="dd"
if type(a) is int:    #type(a)用来判断数据类型
    print("是数字")
elif type(a) is str:
    print("是字符")
else:
    print("是其他")
"""

#循环    while for
"""

a= 1
while a<10:
    print("haha",a)
    a = a+2
"""
#遍历，每个值都读一遍包括符号
"""
a = "你好,今天你吃了吗?"
for i in a:
    print (i)   #print循环的运行了10遍

for i in range(0,100):   #左闭右开  到99
    print(i)

b =list(range(0,100,3))  #list数组   3为步进/步长 显示0，3，6，9
print(b)
"""

for i in range(0,10):
    if i == 4:
        continue             #i=4 结束本次跳过，开始下一个循环
    print(i)                 #break  终止循环到此为止以后都别玩了。 嵌套循环时只针对一层终止=continue 