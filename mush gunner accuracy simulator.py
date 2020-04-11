import random

shots=0
hits=0
kills=0
misses=0 #misses IN A ROW
damaged=False

while shots<1000000:
    n=random.randint(1,101)
    shots+=1
    
    if misses==0:
        if n<=60:
            hits+=1
            m=random.randint(1,6)
            if m>=3 or (m<3 and damaged==True):
                kills+=1
                damaged=False
            else:
                damaged=True
        else:
            misses=1 
            
    elif misses==1:
        if n<=90:
            hits+=1
            misses=0
            m=random.randint(1,6)
            if m>=3 or (m<3 and damaged==True):
                kills+=1
                damaged=False
            else:
                damaged=True
        else:
            misses=2
            
    elif misses==2:
        if n<=99:
            hits+=1
            misses=0
            m=random.randint(1,6)
            if m>=3 or (m<3 and damaged==True):
                kills+=1
                damaged=False
            else:
                damaged=True

print ("Out of "+str(shots)+" shots")
print(str(hits)+" hits")
print(str(kills)+" kills")