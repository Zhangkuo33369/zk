"""
   python的一些小技巧
   python对文件的读写
"""
import time
now =time.strftime("%y-%m-%d %H:%M:%S")
text = input("请输入心情: ")
with open("C:\workhome/日记.txt","a",encoding="utf8")as f:    
    f.write(now +"\n") 
    f.write(text +"\n")                           
    f.write("-----------------------\n")
"""
右下角utf8可以控制乱码，""GBK""
"a"追加保存，"w"写入不保存

"""

"""
    python制表符  \n 换行
                 \t 自动添加tab
"""