def factoriel1(n):
    if n==0 or n==1:
        res=1
    res=1
    i=1
    while i<=n:
        res=res*i
        i=i+1
    return res

def factoriel2(n):
    if n==1:
        return n
    else:
        return n*factoriel2(n-1)

def puiss1(x,y):
    res=1
    i=1
    while i<=y:
        res=res*x
        i=i+1
    return res

def puiss2(x,y):
    if y==1:
        return x
    else:
        return x*puiss2(x,y-1)
    
def etoiles1(n):
    i=1
    while i<=n:
        print('*'*i)
        i += 1

def etoiles2(n):
    if n==1:
        print('*')
    else:
        print('*'*n)
        return etoiles2(n-1)

def etoiles3(n):
    if n>0:
        etoiles3(n-1)
        print('*'*n)

##tournoi de hanoi
def hanoi(n,src,temp,dest):
    if n==1:
        print(src,'-->',dest)
    else:
        hanoi(n-1,src,dest,temp)
        print(src,'-->',dest)
        hanoi(n-1,temp,src,dest)

def binaire(n):
    if n>1:
        binaire(n//2)
    print(n%2,end='')

        


    

    
    
       
        


    
        
