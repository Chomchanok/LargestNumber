list = [50,2,1,9]
def split(list):
   spd= []
   for i in range(len(list)):
       newlist = [int(a) for a in str(list[i])]
      
       spd.append(newlist)
   return spd

def SortNum(spd):
    
# Swap the elements to arrange in order
    for i in range(len(spd)):
        
        for idx in range(i):
            
            if spd[i] > spd[idx]:
                spd[i],spd[idx] = spd[idx],spd[i] 
    arrayConcat = []
    stringC = ""

    for i in spd: 
    
        for j in i:
            arrayConcat.append(str(j))
            
    for i in arrayConcat:
         stringC = stringC + i 

    print(stringC)      
                
   

        
        
SortNum(split(list))