import random

shots=0
hits=0
kills=0
misses=0 #misses IN A ROW

while shots<1000000:
    n=random.randint(1,101)
    shots+=1
    
    if misses==0:
        if n<=66:
            hits+=1
            kills+=1
        else:
            misses=1 
            
    elif misses==1:
        if n<=99:
            hits+=1
            kills+=1
            misses=0

print ("Out of "+str(shots)+" shots")
print(str(hits)+" hits")
print(str(kills)+" kills")