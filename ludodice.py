n = input("enter your name")
a = '''
  -------
 |   .   |
 |       |
  -------

 '''
b = '''
  -------
 |   ..  |
 |       |
  -------

 '''
c = '''
  -------
 |  ...  |
 |       |
  -------

 '''

d = '''
  -------
 |   ..  |
 |   ..  |
  -------
# '''
e = '''
-------
|  ...  |
|  ..   |
 -------

'''
f = '''
 -------
|  ...  |
|  ...  |
 -------

'''
l = [a,b,c,d,e,f]
import random
c = random.randint(1,6)
if c == 6:
     print(l[c-1],end='\n')
     print(n,'hurrey you got 6*3=18 chocolates:')
     print(n,'you have earned yourself a second chance:')
     c =random.randint(1,5)
     print(l[c-1])
     print(n,'you have got',c*2,'extra chocolate')
     print(n,'totaly you have earned',c*2+18,'chocolates')
elif c==5 or c==4:
     print(l[c-1],end='\n')
     print(n,'totaly you have earned',c*2,'chocolates')
elif c==2 or c==3:
     print(l[c-1],end='\n')
     print(n,'totaly you have earned',c,'chocolates')
else:
    print(l[c-1])
    print(n,'ayyo sorry thats the least dies you have not earned any chocolates')
