# prime  number  : its only two factors --->1 ,number itself
"""
4 factors : 1,2,4 
19 factors  : 1,19 
33 factors : 1,3,11,33
77 factors : 1,7,11,77
31 factors : 1,31

"""

"""
num =int(input("enter the number"))  # 5
count =0   # 0 

for i in range(1,num+1):  # 5,6
    if num % i ==0 :      # 5 % 5==0 
        count +=1          # 2
if count ==2 :   # 2==2
    print(num,"is a prime number")
else :
    print(num,"is not a prime number")

"""

# perfect number  : 

"""
6 factors : 1,2,3 
sum factors : 1+2+3 = 6   -----> perfect number 

28 factors  :1,2,4,7,14 
sum factors : 1+2+4+7+14 = 28  -----> perfect number

100 factors  : not  perfect number  

"""
"""
num =int(input("enter the number"))  # 6
sum =0   # 0 

for i in range(1,num):  # 5, 6
    if num % i ==0 :      #  6 % 5 ==0 
        sum =sum +i          # sum =6
if sum ==num :   # 6==6
    print(num,"is a perfect number")
else :
    print(num,"is not a perfect number")
"""


# while  loop  : 

"""
syntax : 

i=intalization 
while condition : 
    print()
    inc/dec
"""

# 1-100 : 

"""
i=1 
while i <=100 :
    print(i)
    i+=1   # i = i +1 
"""
    
# using while solution of  AMG : 

# armstrong number  :
"""

153 : 

1**3   5**3   3**3  
1       125    27 
sum = 1+125 +27 =153  ------> amg  

1634 :  4 digit 
1 **4   6**4   3**4    4**4 
1       1296    81      256 

sum = 1+1296+81+256 =1634  -----> armstrong number

logic  : 1634

1. len fuction , type casting  ----> how many digits --->digits  --->4 
2. r = num % 10  ----> 1 % 10 = 1  
3. power = pow(r,digits) ----> 256
4. sum =sum +power   ----> sum = 0 +256 =256  
5. num = num //10   ----> 16 //10 ---> 1 
--- > sum =sum + pow(r,digits)  ----> sum = 1634 
"""

"""num =int(input("enter the number"))  # 1634
sum =0 
digits = len(str(num))   # 4
temp =num   # temp =1634 
while  temp > 0  :  # 0 > 0 
    r= temp % 10     # r = 1 % 10 =1 
    sum = sum + pow(r,digits)  # sum =1634  
    temp = temp //10  # temp  =0 
    
if sum ==num :  # 1634 == 1634 
    print(num,"is a armstrong number")
else :
    print(num,"is not a armstrong number")
"""    

# reverse  number  :

"""
user =123 
ouput : 321 

logic :   rev =0 
1. num % 10 ---->1 %10 = 1  
2. rev = rev * 10 +3  ----> rev ==321  
3. num = num //10   ----> 1 //10  --->0 

"""

"""
num =int(input("enter the number"))  
rev = 0 

while num > 0 :
    r= num % 10
    rev = rev * 10 + r
    num = num //10
print("reverse number is :",rev)
"""

# palindrome  number  : 
"""
reverse also getting  same  number  : 
ex : 121  ---->121  ,131 ,11  ,22  

"""

"""
num =int(input("enter the number"))  
rev = 0 
temp =num 
while temp > 0 :
    r= temp % 10
    rev = rev * 10 + r
    temp = temp //10
if num ==rev :
    print("pelindrome number")
else :
    print("not pelindrome number")

"""

# task :1 
"""
ask user to enter  the  and check  it is  twin number  or  not . 

each digit sum 
each  digit multiply     
sum == multiply

ex : 
input  :123 
each digit sum : 1+2+3 =6 
each digit multiply : 1*2*3 =6
sum == multiply : 6 == 6
output : twin number
"""

