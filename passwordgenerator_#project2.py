from random import *
print('** Welcome to password generator !')
letters=int(input('enter no. of letters you want in password'))
digits=int(input('enter no. of digits you want in password'))
symbols=int(input('enter no. of symbols you want in password'))
password=''
password1=''
password_list=[]
for i in range(0,letters):
    password=password+str(chr(randint(65,90)))
   
#print(password)
for j in range(0,digits):
    password=password+str(randint(0,9))
#print(password)
for k in range(0,symbols):
    password=password+str(chr(randint(35,38)))
#print(password)
'''for i in range(0,letters+digits+symbols):
    password+=str(chr(randint(33,122)))
print(password)'''
for i in password:
    password_list+=i
#print(password_list)
shuffle(password_list)
#print(password_list)
for i in password_list:
    password1+=i
print('generated password : ',password1)

