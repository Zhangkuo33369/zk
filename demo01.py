"""
print ("hello world!")  #字符串#
print (())              #元组
print ([])              #数组
print ({})              #字典
多行注释三个引号，一定要英文符号
啊啊啊啊啊
这玩意得单独另起一排还得顶格写
算了以后#方便，一行一个#呗

print("haha",23333,1.02) #输出多值
print("wo"+"cao")  #字符串的拼接，只能同类型操作不可以字符串加
                        #数字啥的
print(((1+2)*100-9.0)/2)    
print(2>3)    
name = "张三"   #把张三这个赋值付给了名字叫name的这个变量  
""" 
     

#数据格式的转换 
# print(type(22))
# print(type("hello"))
# print(type(2.2))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))
"""鼠标选中然后 ctrl+/ 能同时给他们加字符 问号那个键
#除了空，任何数据类型都可以转换为str
#int float可以互相转换
#str转换成其他需要满足长得像
"""
#a=int(2666)
#print(type(a) ) 这是用看是什么数据类型的
"""
a = input("请输入:")
b = input("请输入:")
print("input获取的内容:",a+b)  #input出来都是字符串，相加默认拼接   
"""
"""
a =   int (input("请输入:"))
b =   int (input("请输入:"))
print("input获取的内容:",a+b)
"""
#len()查看字符长度不可以查看intfloat
"""
a = "哈哈哈bs"
print(len(a))
"""



a = input("请输入:")
b = input("请输入:")
print("两端字符串长度是:",len(a)+len(b))