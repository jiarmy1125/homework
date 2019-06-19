from random import *

a=1
b=[] #列出20個亂數的陣列
x=[] #取出兩位數的陣列
y=[] #偶數陣列
z=[] #奇數陣列
while a <= 20: 
    c=randint(1,200)        #亂數取出20個數字
    if c not in b:          #判斷數字是否重複
        b.append(c)
        a=a+1        
        if c>9 and c<99:    #判斷是否為兩位數
            x.append(c)
            if c%2==0:      #判斷是否為偶數
                y.append(c)

            else:           #奇數
                z.append(c) 

print("取出陣列"+str(b)) 
print("陣列長度："+str(len(b))) 
print("兩位數"+str(x))    
print("偶數"+str(y))
print("奇數"+str(z))