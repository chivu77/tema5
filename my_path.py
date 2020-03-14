nr_verificate=0
nr_nrprime=0
nr_perfecte=0
import math

def estePrim(x):
    global nr_nrprime
    global nr_verificate
    isPrime=1
    for i in range(2,x//2+1):
            if x%i==0:
                isPrime=0
                break
    if isPrime==1:
         nr_nrprime=nr_nrprime+1
    nr_verificate=nr_verificate+1
    print(nr_nrprime)
    print(nr_verificate)
            

def patratPerfect(numar):
    global nr_perfecte
    if int(math.sqrt(numar)) == math.sqrt(numar):
             nr_perfecte=nr_perfecte+1
    print(nr_perfecte)
         
if __name__=="__main__": 
    adevar='y'
    while adevar=='y':
        x=int(input("introdu nr:"))
        
        estePrim(x)
        patratPerfect(x)   
        print(nr_verificate)
        print(nr_nrprime)
        print(nr_perfecte)
        print("doresti sa continui?y/n")
        adevar=input()