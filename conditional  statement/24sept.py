"""
task :1 

ask user to enter the  3 subjects marks  and calculate the  percentage  and based on percentage  give the  grade.

Grade     percentage 
above 90   A+ 
80-90      A 
70-80      B+
60-70      B
50-60      C+
40-50      C
below 40   Fail

task :2 
ask user to enter to enter the  salary and calculate the basic  salary. 

basic salary  = salary  +HRA +DA 

range           HRA     DA 
<10000          20%     60% 
10000-20000     25%     75%
above 20000     30%     80%

hint  : salary  =int(input("enter the salary :"))  # 5000 
if salary <10000 :
    hra = salary * 0.20   # 1000
    da = salary * 0.60    # 3000
    total salary = salary + hra +da     =====>  5000 + 1000 +3000 =9000
    print("basic salary :",total salary)

task :3 
ask user to enter the character/string and check it's  vowel or  consonant or digits or special character. 

"""
# solution  :1 

phy =int(input("enter the phy :"))   # 89 
maths =int(input("enter the maths :"))  # 78
chemistry =int(input("enter the chemistry :")) # 90 

percentage = (phy + maths + chemistry)/3
print("percent :",percentage)

if percentage >90 :
    print("GRADE :A+")
elif percentage > 80 and percentage <=90 :
    print("GRADE :A")
elif percentage > 70 and percentage <=80 :
    print("GRADE :B+")
elif percentage > 60 and percentage <=70 :
    print("GRADE :B")
elif percentage > 50 and percentage <=60 :
    print("GRADE :C+")
elif percentage > 40 and percentage <=50 :
    print("GRADE :C")
else :
    print("GRADE :Fail")