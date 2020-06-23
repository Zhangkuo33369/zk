#方法/循环

"""
#自动判断账号长度5---8位且小写
def checkname(username):       #方法的声明  方法的名字（可省略）  方法的参数
    
    #自动判断账号长度5---8位且小写
    
    if len(username) >=5 and len(username) <=8 :         #方法的逻辑代码
        if username[0] in "dqedfregfgft":       
            print("ok!")
        else:
            print("必须小写！")    
    else:
        print("账号不符合")
checkname("7dfsdf")
# a = "7dfsdf"
# checkname(a)
checkname()                        
"""         
#""""里面不能有"""了！且必须顶头 ，#不显示说明只有"""才显示且必须tab对其

def jiafa(a,b):
    """ 
    这个方法的作用是相加
    """
    if type(a) is int and type(b) is int:
        print(a+b)
    else:    
        print("滚")
jiafa(22,52)
                   




