 #学生成绩录入系统，名字成绩对应上  (用字典能一一 对应键值对)
 #60上下分开存放                   （数组/字典）
"""
highchengji ={} #定义了一个空字典用来存储大于60的信息
lowchengji ={}  #定义了一个空字典用来存储小于60的信息
studentlist =["z","x","c","v","b","n","m"] 
a = 0   #定义一个变量控制数组下标
while a < len(studentlist):  #所有信息输入都要input，所以写了个循环，len判断数组长度，总长度-1就是最大下标
    chengji=int ( input("请输入"+studentlist[a]+"的成绩:") )#录入信息为了方便判断所以转换了格式
    if chengji >= 60 :
        highchengji[studentlist[a]]=chengji   #新增到字典中
    else :
        lowchengji[studentlist[a]]=chengji   
    a = a + 1
print("大于60的:",highchengji)
print("小于60的:",lowchengji)


"""
"""
highchengji ={} 
lowchengji ={}  
studentlist =["z","x","c","v","b","n","m"]    
for i in studentlist:  
    chengji=int ( input("请输入"+i+"的成绩:") )
    if chengji >= 60 :
        highchengji[i]=chengji  
    else:    
        lowchengji[i]=chengji   
print("大于60的:",highchengji)
print("小于60的:",lowchengji)
"""




"""
#作业
#获取用户的个人信息并储存到字典中
name = input("请输入你的姓名:")
age = input("请输入年龄:")
sex = input("请输入性别:")
userinfo={}
userinfo.update(name=name,age=age,sex=sex)
# userinfo["name"]=name
# userinfo["age"]=age
# userinfo["sex"]=sex
print(userinfo)
"""

"""
#乘法表练习
for i in range(1,10):  #从1到9  冒号让你吃了！！！！？
    for j in range(1,i+1):    #第一次循环（1，2）只有1   第二次循环（1，3） 有1，2 第三次（1，4）有1，2，3
        print(i,"*",j,"=",i*j,end="  ")# end控制不换行，里面空格控制排版距离
    print()                            #这里的print起换行作用
"""
#无限循环红灯35次绿灯30次黄灯5次

# light = {"红灯":30,"绿灯":35,"黄灯":3 }
# for i in light:
#     print(i)    #这里print的是key，红灯红灯红灯红灯这样，不是value

"""
light = {"红灯":30,"绿灯":35,"黄灯":3 }         #字典可维护性很高，直接在这就可以改不需要动代码
while True :                                   #无限死循环  也可以while 1 ：
    for i in light:                            #循环key
        for j in range(light[i]):              #循环value次数
            print(i,"倒计时还有",light[i] -j,"秒")    #30-0=30  30-1=29 ...

"""




"""
#实现注册功能，用户输入账号和密码，账号5到8  密码 6到12位  账号必须小写开头 {username：password}
#的形式储存到字典中

username = input ("请输入账号:")
password = input ("请输入密码:")
if len(username) >=5 and len(username) <=8 :
    if username[0] in "dqedfregfgft":       #账号首字母为小写
        print("ok")
        if len(password) >=6 and len(password) <=12 :
            print("成功")
        else:
            print("密码不符！") 
    else:
        print("必须小写！")    
else:
    print("账号不符合")

""" 
def checkname(username,password):    
    if len(username) >=5 and len(username) <=8 :
        if username[0] in "dqedfregfgft":       #账号首字母为小写
            return("ok")
            if len(password) >=6 and len(password) <=12 :
                return("成功")
            else:
                return("密码不符！") 
        else:
            return("必须小写！")    
    else:
        return("账号不符合")
checkname("asdfgh","sasasss")
print(checkname("asd","sasasss"))