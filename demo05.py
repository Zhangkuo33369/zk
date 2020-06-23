def jiafa(a,b):
     """ 
     这个方法的作用是相加
     """
     if type(a) is int and type(b) is int:
         return(a+b)
     else:    
         return("滚")

#print( jiafa(22,52) )  
#不写return直接print下面会显示null，写了return最后在print有返回值，返回之后还可以做其它操作
#return拿到结果可以接着做其他事情
a = jiafa(1,2)
print(a+2)

#异常处理/捕获  搭配使用    为了控制用户输入的数据 六十七
try:
    print(s+2)
except :
    print("上面写错了")

#包》模块》类》方法》变量   包含且并列（都可以单独拿出来使用，变量a=1，方法b=jiafa（1，1）） .py模块
# print，jiafa，都是方法
# 异常类（处理代码报错告诉你哪错了）   
 
try:
    print(s+2)     #这里如果是正确的正常运行不输出下面的，直接输出正确的。上面的错了才输入下面的
except Exception as e:
    print("上面写错了",e)   #e告诉你错在哪


#包的运用  python自带包
import time        #一般放在顶部
for i in range(10):
    time.sleep(1)  #每个一秒遍历一个
    print(i) 

"""    
import random生成随机数
a = random.randint(100,1000)
print(a)
"""
"""
 第三方的包 pip install 包名
           pip uninstall 包名
           pip list      
 这些在终端操作也可以在cmd上弄（直接在下面弄）  与loadrunner冲突，，需要pip3  ~~~~   位置在环境变量根目录里面
"""                   