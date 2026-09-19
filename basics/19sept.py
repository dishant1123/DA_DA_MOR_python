# variable  rules : 
"""
1. start number ,special character , middle special character  ---->not valid 
    ex : @a=90 ,a@=78 ,12a =89 
2. exception  : underscore (_)  ----> valid 
    ex : _ =90 , a_=89 ,a_a =56 ,d__ =89 
3. end number  ----> valid  

    ex : a12 =90 

"""

# data type   :
"""
1. int  : positive or negative integer / values 
2. float : positive or negative float / values   ----> decimal  
3. char /string :  a to z , special character , numbers , underscore 
4. boolean : true or false
5. complex number : i or  j  
    2 part -----> 1. real number  2. imaginary number
    78 +12j ----> 78 real number , 12j imaginary number
"""

"""
a=90567856756756767 
print(a)
print(type(a))  # type  casting  -----> int 
print("a value is  :",a)
print("a=",a)

b=902345.561234534564567 
print(b)
print(type(b))  # type  casting  -----> float
print("b value is  :",b)
print("b=",b) 

c="het"
print(c)
print(type(c))  # type  casting  -----> string
print("c value is  :",c)

d=True
print(d)
print(type(d))  # type  casting  -----> boolean

f= 23+90j 
print(f)
print(type(f))  # type  casting  -----> complex number

g=90 +56j 
print(f+g)
"""

# user input  :  int  ,float 

"""a=int(input("enter the a value  :"))
b=int(input("enter the b value  :"))

print("a=",a)
print("b=",b) 
print(a+b)
# note  : int  data type  can't  store  float  value. 
"""

# float :
"""x=float(input("enter the x value  :"))
y=float(input("enter the y value  :"))

print(x)
print(y)
# note : float  data type  can  store  int  value.
"""

# string :

"""
name=str(input("enter the name  :"))
surname=input("enter the sur-name  :")

print(name,end=" ")
print(surname)
# dishant shah
"""
"""
task :1 
ask user to enter the  two  int  type  number and  print the  division  result.

task :2 
ask user to enter the  two  int type  value and  concate  them. 
input  a= 90 
input  b=56 

output  : 9056 

"""
