"""
pattern  : 

1.          2.          3.           4.           5.          6.
* * * * *   *           * * * * *    1            5 4 3 2 1   1
* * * * *   * *         * * * *      1 2          5 4 3 2     1 4 
* * * * *   * * *       * * *        1 2 3        5 4 3       1 4 9
* * * * *   * * * *     * *          1 2 3 4      5 4         1 4 9 16  
* * * * *   * * * * *   *            1 2 3 4 5    5           1 4 9 16 25


7.           8.           9.         10.           11.
* * * * *    * * * * *          *         *               * 
  * * * *     * * * *         * *        * *             * * 
    * * *      * * *        * * *       * * *           * * *  
      * *       * *       * * * *      * * * *         * * * *
        *        *      * * * * *     * * * * *       * * * * * 
                                                       * * * *
                                                        * * *
                                                         * * 
                                                          * 
 
"""

# task: 1 ask user to  enter the two range  that start range and ending range print  prime  number  between  two  range. 

"""
start = int(input("enter the start range: "))  # 10 
end = int(input("enter the end range: "))  # 200 

for i in range(start, end+1):   # 11 , 201
    count =0              # count =0 
    for j in range(1, i+1) :  # 1,12 
        if i % j==0 :      #10 % 10  ==0  
            count +=1       # count =2
    if count==2:   # 2==2
        print(i,end=" ")  # 11 
"""
# 1 : 

"""
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
"""
# 2 :
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

# 3 :
"""
for i in range(1,6):
    for j in range(6,i,-1):
        print("*",end=" ")
    print()
"""

# 7 :
"""for i in range(1,6):  # 2 
    for k in range(1,i):  # 1,2
        print(" ",end=" ")
    for j in range(6,i,-1):  # 6 , 2 ,-1
        print("*",end=" ")   #  * * * * * 
    print()                  #    * * * * 
"""
# 8 :
"""
for i in range(1,6):  # 2 
    for k in range(1,i):  # 1,2
        print(" ",end="")
    for j in range(6,i,-1):  # 6 , 2 ,-1
        print("*",end=" ")   #  * * * * * 
    print()                  #   * * * * 

"""

# 9 : 
"""
for i in range(1,6):
    for k in range(5,i,-1) : 
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

# 10 :
"""
for i in range(1,6):
    for k in range(5,i,-1) : 
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

# 11 : 

for i in range(1,6):
    for k in range(5,i,-1) : 
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,6):  # 2 
    for k in range(1,i):  # 1,2
        print(" ",end="")
    for j in range(6,i,-1):  # 6 , 2 ,-1
        print("*",end=" ")   #  * * * * * 
    print()                  #   * * * * 
