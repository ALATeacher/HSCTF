'''
Created on May 10, 2018

@author: ncarlson
'''
def letter(num):
    if num==27:
        return " "
    elif num==28:
        return "_"
    else:
        return chr(num+96)
    
def base3(num):
    s = str(num)
    l = len(s)
    n = 0
    total = 0
    while n<l:
        mult = pow(3,(l-n-1))
        total+=mult*int(s[n])
        n+=1
    return total

flag = "22 12 200 12 1000 212 12 1000 210 201 12 1000 202 12 200 112 1 200 221 1000 202 120 1000 21 12 202 1000 202 22 12 1000 20 110 1 21 1000 202 22 200 12 12 1001 11 100 21 100 202 201 1001 100 201 112 202 1001 211 12 200 221 1001 201 12 10 210 200 12"
flag = flag.split(" ")
s = ""
for x in flag:
    s+=letter(base3(x))
print(s)

def change2(input):
    vary = [1,7,5,3,5,4,2,6,3]
    pw = ""
    for i in range(9):
        num = ord(input[i])-96+vary[i]
        pw+=letter(num)
    return pw

def change1(input):
    vary = [4,3,5,6,1,2,3,3,1]
    pw = ""
    for i in range(9):
        num = ord(input[i])-96-vary[i]
        pw+=letter(num)
    return pw
        
print(change1(change2("djckktjbq")))