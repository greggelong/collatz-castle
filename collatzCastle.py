# i could recast all as ints but it doesnt really matter to python
# or just print door and rooms as ints

import random



def check3np1(num):
    if num%2 ==0:
        if (num-1)%3 == 0:
            print(num, (num-1)/3, "or", num*2, "or" ,num/2 )
            return True
        else:
            print(num, "not 3np1", num*2 , "or",num/2)
            return False
    else:
        print( num, "is odd so 3np1" , num*3+1, "or", num*2)
        return True



def collatzNeighbors(num):
    ''' get the collatz neighbors of a number
        return as a immutable tuple'''
    if num%2 ==0:
        # form 3np1 factor
        if (num-1)%3 == 0:       
            #print(num, (num-1)/3, "or", num*2, "or" ,num/2 )
            return ((num-1)/3, num*2, num/2)
        else:
        # not 3np1 factor
            #print(num, "not 3np1", num*2 , "or",num/2)
            return (num*2, num/2)
    else:
        # cant divide by two as its odd so 3np1 and mult by 2
        #print( num, "is odd so 3np1" , num*3+1, "or", num*2)
        return (num*3+1, num*2)
    
    
def collatzpath(num):
    ''' returns a list of the collatz path from the number
        all the way to one.  in the game this is the map'''
    
    path = []
    path.append(num)
    while num > 1:
        if num%2 == 0:
            num = num/ 2
            path.append(num)
        else:
            num = num*3+1
            path.append(num)
    return path
    
    
def collatzgame():
    ## get a random starting point
    steps = 1
    mynum = random.randint(10,100)
    mymap = collatzpath(mynum)
    print("-/-"*10)
    print("ESCAPE FROM COLLATZ CASTLE")
    print("-/-"*10)
    print("you have randomly materialized in rooom", mynum)
    print("You escape when you reach room 1")
    print("There is a path to get you there")
    print(f"That path has {len(mymap)-1} steps")
    print("map: ", mymap)
     
    # game loop 
    while mynum >1:
        ##
        numNeigh = collatzNeighbors(mynum)
        
        print("-/-"*8)
        print("step: ",steps)
        print(f"You are in room {mynum} , there are {len(numNeigh)} doors")
        
        mychoice = 0
        while mychoice not in numNeigh:
            for i in numNeigh:
                print(f"***{int(i)}*****")
            mychoice = int(input("Please choose from the above doors. >>"))
        
        mynum = mychoice
        steps +=1
    print("*"*18)
    print("YOU HAVE ESCAPED COLLATZ CASTLE")
        
                    
 

collatzgame()

 


# return all the other nodes for number and generate a room escape game
