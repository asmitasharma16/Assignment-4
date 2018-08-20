#Q.1- Reverse the whole list using list methods.
l=[1,2,3,4,5]
print('list = ',l)
#method 1
l.reverse( )
print(l)
#method 2
l=[1,2,3,4,5]
print(l[::-1])
#method 3
l=[1,2,3,4,5]
print(list(reversed(l)))

#Q.2- Print all the uppercase letters from a string.
string =input("enter string ")
ustring=''
for char in string:
    if(char.isupper()==True):
        ustring+=char
print(ustring)

#Q.3- Split the user input on comma's and store the values in a list as integers.
num=input('input ').split(' ')
print('number in string form ',num)
newnum=[ ]
for i in num:
    newnum.append(int(i))
num=newnum
print('number in int form ',num)

#Q.4- Check whether a string is palindromic or not.
#eg string= "iTopiNonAvevanoNipoti" is palindrome 
string=input("Enter a string ")
string=string.lower( )
rstring=' '
rstring=string[::-1]
print(string)
print(rstring)
if(string==rstring):
    print('string is palindromic')
else:
    print('string is not  palindromic')

#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
#In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.
import copy as c
l1=[1,2,[3,4],5]
#using deepcopy to deep copy
l2=c.deepcopy(l1)
print('original list ',l1)
l2[2][0]=100
print('New list after deep copy ',l2)
#changes not reflected in original list as it is deep copy
print('original list after deep copying ',l1)
#In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.
l1=[1,2,[3,4],5]
#using copy to shallow copy
l2=c.copy(l1)
print('original list ',l1)
l2[2][0]=100
print('New list after shallow copy ',l2)
#changes are reflected in original list as it is shallow copy
print('original list after shallow copying ',l1)


        
        
    
