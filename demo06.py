#import pymysql     #导入使用pymysql(连接数据库的)

"""
类 class声明类的名字，首字母必须大写 class Test()      (方法def)
面向对象编程 
类里面的所有方法必须传一个参数self
"""
class GirlFriend():
    def __init__(self):           #初始化  这里是写死了 
        self.sex="女"
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
wanqian = GirlFriend()                                #死的
wanqian.caiyi(3)
wanqian.work()
print(wanqian.high)

class Fangzi():
    def __init__(self,sex,high,weight):           #初始化  这里是写活了
        self.sex=sex
        self.high=high
        self.weight=weight
    def Fly(self):
        print("起飞")    
liuyifei = Fangzi ("女","170cm","120")             #活的，填数据
liuyifei.Fly() 
    

#类的继承 pass无意义怕没写完报错
class Nvpengyou(Fangzi):
    pass
liuyifei = Nvpengyou("女","170cm","120") 
liuyifei.Fly()
"""
   Fangzi父类
   Nvpengyou子类
"""