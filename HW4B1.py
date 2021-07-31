import itertools  # using combinatoric iterators
listA =  [50,1,2,9]#[10,1]#[121, 1, 2, 50]#[50,1,2,9]
perm = itertools.permutations(listA) #using permutation to arrange number in listA
newlist = [] #create newlist to collect number after rearrangement
for i in list(perm): 
    arrayConcat = [] # create arrayConcat list to collect every posible number 
    stringC = "" # create stringC to merge every number in arrayConcat list and tranform to string type
    #print(i)
    for j in i:
        arrayConcat.append(str(j)) # collect every possible patterns
    #print(arrayConcat)
    for key in arrayConcat:
        stringC += key # merge number in list to string
    print(stringC)   
    for s in stringC: 
        newlist.append(stringC)
print(max(newlist)) # finding max value in newlist and show output
    
         
                
   

        
        
