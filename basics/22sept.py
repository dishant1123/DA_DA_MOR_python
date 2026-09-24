# operator  : 
"""
1. airthematic : + - * / //  %  
2. comparison : ==  !=  >  <  >=  <=    ====> asnwer in  boolean  format
3. assignment : =  +=  -=  *=  /=  //=  %=  **=  //=  %=
4. logical : and , or  
5. member : in  ,not in
"""
a=20
b=10

# print(a+b)
# print(a/b)  # 10 /30   = 0.3
# print(a//b)  # floor division  : int  value  : 10 /30 = 0 
# print(a%b)   # modulas : remainder  : 10 % 30 =  ??

# print(a!=b)

# a= a+b  a= a-b  a=a *b   a= a/b   
# a+=b    # a-=b    a*=b    a/=b
# print(a)

"""a=34
b=100
"""
# print(a>=b and  a==b)  # 
# print(a>b or  a!=b)  # 


"""l1=[1,2,3,4,5]

print(3 in l1)
print(8 not in l1)
"""
# conversion  : 

"""
a =90 
print(a)
print(type(a))
# convert a value  in to the  float   
print("a value  convert into  the  float :",float(a))
print("a value  convert into  the  string :",str(a))
"""

# conditional  statements : 
"""
1. if else : 

syntax :

if (condition):
    print()
else :
    print()

"""

# ex :1 ask user  to enter the age and  check its eligible for  vote  or not 

"""
age=int(input("enter your age :")) 

if age>18 :  # 12 > 18 
    print("eligible for vote")
else :
    print("not eligible for vote")
    
"""
# ex :2 ask user to enter  the two  number and check  which  one  is  big. 

"""
a=int(input("enter the first number :"))  # 232  
b=int(input("enter the second number :"))  # 45

if a>b :
    print("a is big")
else :
    print("b is big")
"""
# ex :3 ask user to enter the number and  check  if its even or odd

"""
num = int(input("enter the number :"))
if num % 2 ==0 :
    print("even")
else :
    print("odd")   
"""    
   
# ex :4 ask  user to enter the  number and check its divisible  by  5 or not . 

"""num = int(input("enter the number :"))
if num % 5 ==0 :
    print("div by  5 ")
else :
    print("not")   
"""

# nested if : 
"""
syntax : 

if  con :
    print () 
elif con : 
    print()
else :
    print()

"""

"""a=int(input("enter the first number :"))  # 10
b=int(input("enter the second number :"))  # 12

if a>b :   # 12 >12 
    print("a is big")
elif b>a :  # 12 >12 
    print("b is big")
else :
    print("same")
"""

# ex :5  ask user to enter the number and  check  number is div by  5  or  11 or both . 

"""num = int(input("enter the number :"))  # 55 

if  num % 5==0 and num % 11 ==0 :
    print("div by  5 and 11 both ")

elif num % 11 ==0 :
    print("div by  11")
   
elif num % 5 ==0 :
    print("div by  5 ")

else :
    print("not div by  5 or 11")
"""

"""
1. ask user to enter the  radius and calculate the area of the circle. 
    area of circle = 3.14 * r * r 
    
2. ask user  to enter the 3 number and  check  the which number is  big 
    input  a =90 b=56 c =23   -----> output  a is big
    
"""
# logic : 
"""
a  -----> a>b  a>c 
b  -----> b>a  b>c
c  -----> c>b  c>a

"""


a=int(input("enter the a value :"))
b=int(input("enter the b value :"))
c=int(input("enter the c value :"))

if a>b  and a>c :
    print("a is big")
elif b>a  and b>c :
    print("b is big")
elif c>a  and c>b :
    print("c is big")
else :
    print("all are small")
    
"""
ask user to enter the three side of  the triangle and check whether  triangle is  equilateral , isosceles or scalene.

Equilateral Triangle: Has three equal sides and three equal angles, always measuring 60°.

Isosceles Triangle: Has two equal sides and two equal angles.

Scalene Triangle: Has no equal sides and no equal angles  


"""
