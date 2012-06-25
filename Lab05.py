'''
Seth Fiawoo
MIT-AITI 2012
Lab05: Python Functions
'''
#Problem 2
def factorial(num):
    if(num<=0):
        return 1
    else:
        return num*factorial(num-1)
print 'The factorial is',factorial(5)

#Problem 3
def fibonacci(num):
    fibo=[]
    fibo.append(1)
    if(num<=1):
        return fibo
    fibo.append(1)
    if(num==2):
        return fibo
    if (num>2):
        for i in range(2,num):
            temp=fibo[i-1]+fibo[i-2]
            fibo.append(temp)
    return fibo
print 'The fibonacci numbers are',fibonacci(3)

#Problem 4
def prime(num):
    prime=True
    if num==1:
        prime=False
        return prime
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            prime=False
            break
    return prime
print prime(9)

#Problem 5
def isPalindrome(phrase):  
    palindrome=True
    length=len(phrase)
    if len(phrase)%2!=0:
        mid=(length/2)+1
    else:
        mid=(len(phrase)/2)
        
    for i in range(mid):
        if phrase[0-i-1]!=phrase[i]:
            palindrome=False
            break
    return palindrome


print isPalindrome('Able was i ere I saw elba')
    
#Problem 6
def isSubstring(phrase1,phrase2):
    substring=False
    length1=len(phrase1)
    length2=len(phrase2)
    lim=length2-length1+1
    for i in range(lim):
        temp=phrase2[i:length1+i]
        if phrase1==temp:
            substring=True
            break
                
       
    return substring

print isSubstring('ob','foobar')
            
#Problem 7
def maxScore(me,Fred,Jill):
    score=0
    length=len(me)
    for i in range(length):
        if me[i]!=Fred[i] or me[i]!=Jill[i]:
            if Fred[i]==Jill[i]:
                score+=2
            else:
                score+=1
    return score

print maxScore('AAABCDA','ADDBACA','ADCADDC')
            
                    