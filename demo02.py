"""
print (())              #元组
print ([])              #数组
print ({})              #字典
"""

#元组，下标(只想显示的内容)（默认从0个开始）（加[]）
"""
a=(1,2,3,4,"haha","xixi",True)
print(a)
a= (1,2,3,4,"haha","xixi",True)
print(a[4])   #可以倒着数a[-1]
              #切片（批量取值）(只能连着切)
              #print(a[0:4])  zuo闭右开，不包含第四项haha，所以输出为1，2，3，4
              #print(a[4:]) 输出haha和以后
"""
"""
a= (1,2,3,4,"haha","xixi",True)
print(a.index("haha"))     #查找下标，有重复项就近原则 
print(a.count("haha"))     #统计某个值的数量   
"""
"""
#二维元组（元组里面有放了个元组）index和count不能放在二维里
a= (1,2,3,4,"haha","xixi",True)
b=(a,"lala","popo")   #这是三个元素
#print(b[0])
print(b[0][3])   #a输出a里面的4，，，并列的
"""
"""
#数组([])
a= [1,2,3,4,"haha","xixi",True]  #剩下一样的就第一步括号不一样
print(a[4])                      #元组不可以修改，数组可以"."后面的东西多，index，count，
a.append("popopopo")             #从尾巴往里加，这里的加才是修改。直接往里打字不算修改或者说数组能写完之后再修改
                                 #元组有点不想让别人修改写死了用。数组可以修改。
a.insert("popopopo")             #从前面往里加
a.insert( 1,"popopopo")          #上面的0可以省略，随意玩，但不能超出原来的哦 ,这里的1为插入1前面即2之前
                                 #剪切   a.remove()删除值
a.pop(2)                         #直接放数字就可以
b=a.pop(0)                       #剪切后赋值给b
c=a.pop(0)                       #剪切走第一项又剪切走一项   1+2=3
print(b+c)
a.clear()                        #清空
xx =["nihao","buhao"]            #append插得是值，extend是数组
a.extend(xx)   更简单一点print(a+xx)
默认true=1 ，false=0
元组数组字典的取值都是[],
"""


"""
字典{}    
1、字典值没有顺序
2、字典的结构必须是 键值对的结构  key:value   key相当于自定义了下标
3、字典的取值是通过key取value   
"""  

#取值  (通过key取value)
""" 
a={"name":"张三",1:"李白","age":25}         #字符串必须引号
print(a["name"])                           #取值              
a["high"]="175cm"                          #新增
print(a)                                                                              
a["high"]="180cm"                          #修改
print(a)
"""
b=a.get("name")  #取值 （取一个不存在的值get输出为none，用key会报错）
print(b)
b=a.pop("name")  #剪切
a.update(name="赵四") #修改
#数组和字典的删除
del a["name"]
del a[0]
#原来的key存在就是修改，不存在就是新增




