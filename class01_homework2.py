star = int(input("請輸入菱形範圍：")) 
a=star//2+1 #分層製作

for i in range(1,a):            #菱形上半部  1~10
    for j in range(0,(a-i)):    #*前的空白
        print(" ",end="")

    for k in range(0,(2*i-1)):  #從*後開始判斷下一個*的位置
        if k==0 or k==2*i-2:
            print("*",end="")

        else:
            print(" ",end="")

    print(" "+str(i) )

for i in range(a,0,-1):         #菱形下半部 11~1
   
    for j in range((a-i),0,-1): #*前的空白
        print(" ",end="")

    for k in range(0,(2*i-1)):  #從*後開始判斷下一個*的位置
        if k==0 or k==2*i-2:
            print("*",end="")

        else:
            print(" ",end="")

    print(" "+str(i))