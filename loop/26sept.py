"""
loop  :  iteration  ------> repeation. 

type  : 

1.for loop    : entry  control loop 
2.while loop  :exit  control loop

# keyword : 
1.break
2.continue
3.pass 

# for loop  : 
syntax : 

for variable in range(start,stop,step) :
    print(variable)

"""

#  ex :1 print 1 -100
"""
for x in range(1,101) :
    print(x,end=" ") 
print("x value :",x)  # -----> what is  value of  x print  ?? 
"""

# ex :2 odd number  1-100 

"""
for i in range(1,101,2) :  # start : 1 stop :101 step :2 
    print(i,end=" ")  # 1 3 5 7 .... 99
    
"""
# ex :3 
"""
for i in range(1,101,4) :  
    print(i,end=" ")   # 1,4,8 ..
"""

# ex :4 
"""for y in range(100) :
    print(y,end=" ")  
"""

# ex :5 

"""
for i in range(-20 ,20) : 
    print(i,end=" ")  
"""

# ex : 6 100 to 1 
"""
for i in range(100 ,1,-1) : 
    print(i,end=" ")  
"""    

# ex : 7 print 20 to -20 

"""
task :1 print  odd number between  80 to 20 
task :2 print  even number between  20 to 120

"""
# break   : break  and  print 

"""
for i in range(1,10) :
    if i==5 :
        break 
    print(i)
"""
# contunie   : skip iteration  and  contunie the  loop 
"""
for i in range(1,10) :
    if i==5 :
        continue
    print(i)
"""
# pass : pass the  loop ----> when  you  not  break the  loop  and not contunie loop  then use pass . 

"""
for i in range(1,10) :
    if i==5 :
        pass
    print(i)
"""

# ask user to enter the number  and  print n natural  number sum . 
"""
user  =5 
output = 15 ------> 1+2+3+4+5 =15 
"""

"""
num =int(input("enter the number :"))# 6 
sum =0   # sum =1
for  x in  range(1, num +1) :   #  6,7 
    sum =sum +x                 # sum =21
     
print("n natural number sum :",sum)

"""

# ask user to enter the number  and  print n natural  number even sum . 
"""
user  =5 
output = 6 ------> 2+4+ =6 
"""

"""
tasks : 

1. ask user to enter the number  and  print n natural  number odd sum .
2. ask user to enter the number  and  print factorial of the number.
    input  : 5 
    output : 120   ----> 1*2*3*4*5 ---->120 
3. print -30 to 50 
4. ask user  to  enter the  number and check  its prime or  not. 
5. ask user  to enter the  year and check  its leap year or not.


"""
