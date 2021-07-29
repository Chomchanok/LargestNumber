list = [10,1]
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
            
                
    print(spd)
        
SortNum(split(list))
'''
#z = int(str(9) + str(8))
#print(z)

list2 = [121, 1, 2, 50]
[50,2,1,9]

    
array1 = []


for i,word in enumerate(list2):
    
    moveWord = list2[i + 1]
    
    word = str(word)
    word = int(word[0])
'''    
    
       
    
 






