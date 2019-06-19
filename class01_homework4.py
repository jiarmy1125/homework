prime_number=[]
for number in range(2,101):     #2~100，被除數
    for i in range(2,number):   #除數
        r=number%i              #取餘數
        if r==0:                #判斷若餘數等於零，表示不為質數，跳出並繼續做下一個被除數
            break

    else:                       #若為質數，則跳出第二個for迴圈，並印出
        prime_number.append(number)    
    
print(prime_number)
print("質數個數："+str(len(prime_number)))
