def fibonacci(num_1):   #做費氏數列
    if (num_1==0 or num_1==1):  
    #    print(num_1)
        return num_1
        
    else:               
        return fibonacci(num_1-2)+fibonacci(num_1-1)


n = int(input("請輸入第n項：")) 

for num_2 in range(n): #印出結果
    if (num_2==0 or num_2==1):  
        print("Fib(",num_2,") = ",fibonacci(num_2))

    else:
        print("Fib(",num_2,") = Fib(",num_2-2,") + Fib(",num_2-1,") = ",fibonacci(num_2))



#使用for迴圈
# n = int(input("請輸入第n項：")) 

# x=[]
# for num in range(n):    
#     if (num==0 or num==1):  # 0,1
#         x.append(num) #x[0,1]
#         print("Fib(",num,") = ",x[num])

#     else:
#         a=[(x[num-1]+x[num-2])]     #3: 3-1,3-2
#         x += a  #x[0,1,1,........]
#         print("Fib(",num,") = Fib(",(num-2),") + Fib(",(num-1),") = ",x[num])
