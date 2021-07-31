import itertools 
  
listA =  [10,1]##[121, 1, 2, 50]#[50,1,2,9]
perm = itertools.permutations(listA) 
newlist = [] 
for i in list(perm): 
    arrayConcat = []
    stringC = ""
    #print(i)
    for j in i:
        arrayConcat.append(str(j))
    #print(j)
    for i in arrayConcat:
        stringC += i 
    #print(stringC)
      
    for i in stringC:
        newlist.append(stringC)
print(max(newlist))
    
         
                
   

        
        
