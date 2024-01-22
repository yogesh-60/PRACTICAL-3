import random
file=open("practical-3.txt",'w')
length = int(input("Enter the  length of password required :"))
char_included = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456790!@#$%^&*"
i = 0
password = ' '
while i < length :
    password =password + random.choice(char_included)
    i = i +1
file.write(f"Password = {str(password)}")