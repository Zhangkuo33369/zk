#import pymysql     #导入使用pymysql(连接数据库的)

"""
类 class声明类的名字，首字母必须大写 class Test()      (方法def)
面向对象编程 
类里面的所有方法必须传一个参数self
"""
class GirlFriend(object):         #object祖宗类（可省略），下面init其实就是对object的方法做了一个重写
    def __init__(self):           #初始化  
        self.sex="女"              #基本属性  写死了
        self.high="170"
        self.weight="110"

    def caiyi(self,num):             #类里面参数第一个必须self，剩下随便
        print("性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"的别人老婆要给你整：")
        if num ==1:
            print("胸口碎大石")
        elif num ==2:
            print("脚底踩灯泡")
        else:    
            print("裸体斗藏獒")
    def cook(self):
        print("性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"的别人老婆要给你整：")
        print("厨艺牛逼")
    def work(self):
        print("性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"的别人老婆要带你去：")
        print("怡红院头牌")    

#类的实例化
wanqian = GirlFriend()
wanqian.caiyi(3)
wanqian.cook()
wanqian.work()
print(wanqian.high,wanqian.sex,wanqian.weight)

class Baby():
    def __init__(self,sex,high,weight):           #初始化  
        self.sex=sex                              #写活了
        self.high=high
        self.weight=weight
    def fly(self):
        print("爱你")    
liuyifei = Baby ("女","170cm","120")             #活的，填数据
liuyifei.fly() 
    

#类的继承 pass无意义怕没写完报错占个位置
class Nvpengyou(Baby):
    pass
jingtian = Nvpengyou("女","170cm","120") 
jingtian.fly()
"""
   Baby父类
   Nvpengyou子类
   原来的封包了不能动，继承加重写
"""
#类的重写/覆盖  fly一样所以覆盖 
class Nvpengyou(Baby):                           #
     def fly(self):                                
         print("不爱你")  
jingtian = Nvpengyou("女","170cm","120") 
jingtian.fly()
print(jingtian.high,jingtian.sex,jingtian.weight)

