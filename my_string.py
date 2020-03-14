
def f2(s):
    my_dict={}
    for i in range(len(s)):
        if s[i] not in '.,;:/?!':
            counter = s.count(s[i])
            my_dict[s[i]]=counter
            print (my_dict)
  




def f1(sir):
    
    sir=sir.split('.')
    print(sir)
    stringnou=""
    for i in range(len(sir)-1):
        str(sir[i])
        
        stringnou=stringnou+sir[i].capitalize()
        stringnou=stringnou+"."
    print(stringnou) 

if __name__=="__main__":
    sirnou=input("introdu o propozitie:") 
    
    print(sirnou)
    f1(sirnou)
    
    sir2=input("introdu o propozitie:")
    f2(sir2)


