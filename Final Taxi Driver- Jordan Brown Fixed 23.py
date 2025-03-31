#!/usr/bin/env python
# coding: utf-8

# # Jordan Brown
# ## Taxi Driver Program - Artificial Intelligence
# ### 12/10/2023

# In[1]:


import random
import pandas as pd
import time


# ## Taxi Driver Problem - Simple Version (Working)

# In[2]:


print("Town")
# 0 = street, 1 = land/houses, 2 = potential customer

town = [
            [1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]
            ]
print(town)
# town[x] is the row
# town[y] is the column
# town[x][y] is the value at the location 

x= 0
y= 1
z= 0 #counts customers picked up

def xLoc(dropx, dropy, x, y, moves):
    '''
    Renavigates to x Location
    '''
    while x != dropx: # while current x doesn't equal destination x
        if (x < dropx): # if current x is less than destination x
            #print("x is less than dropx")
            if(town[x+1][y] == 0): # if lower location is open, move there
                x+=1
                moves +=1
            else: # when lower location isn't open
                while(town[x+1][y] != 0): # when lower location isn't open
                    if (town[x][y-1] == 0): # if left location is open move there
                        y-=1
                        moves +=1
                    elif(town[x][y+1] == 0): # if right location is open, move there
                        y+=1
                        moves +=1
                continue # go back to while x != dropx
        if (x > dropx): # while current x is greater than destination x
            if town[x-1][y] == 0: # if upper location is free, move there
                x-=1
                moves +=1
            else: # when upper location isn't free
                while(town[x-1][y] != 0): # While upper location isn't free
                    if (town[x][y+1] == 0): # if right location is open, move there
                        y+=1
                        moves +=1
                    elif(town[x][y-1] == 0):
                        y-=1 # if left location is open, move there
                        moves +=1
                continue # go back to while x != dropx
    return x, moves


def GPS (dropx, dropy, x, y, moves):
    '''
    Navigates to the customer's drop off location and drops them off
    '''
    while x != dropx: # while current x doesn't equal destination x
        if (x < dropx): # if current x is less than destination x
            if town[x+1][y] == 0: # if lower location is open, move there
                x+=1
                moves +=1
            else: # when lower location isn't open
                while(town[x+1][y] != 0): # when lower location isn't open
                    if (town[x][y-1] == 0): # if left location is open move there
                        y-=1
                        moves +=1
                    elif(town[x][y+1] == 0): # if right location is open, move there
                        y+=1
                        moves +=1
                continue # go back to while x != dropx
        if (x > dropx): # while current x is greater than destination x
            if town[x-1][y] == 0: # if upper location is free, move there
                x-=1
                moves +=1
            else: # when upper location isn't free
                while(town[x-1][y] != 0): # While upper location isn't free
                    if (town[x][y+1] == 0): # if right location is open, move there
                        y+=1
                        moves +=1
                    elif(town[x][y-1] == 0):
                        y-=1 # if left location is open, move there
                        moves +=1
                continue # go back to while x != dropx
    while y != dropy: # when current y location doesn't equal the y destination
        if (y < dropy): # if current y location is less than y destination
            if town[x][y+1] == 0: # if right location is open, move there
                y+=1
                moves +=1
            else: # if right location isn't open
                while(town[x][y+1] != 0): # when right location isn't open
                    if(town[x-1][y] == 0): # if upper location is open, move there
                        x-=1
                        moves +=1
                    else : # if upper location isn't open, move down
                        x+=1
                        moves +=1
                continue # go back to while y != dropy
        if (y > dropy): # if current y location is greater than y destination
            if town[x][y-1] == 0: # if left is open, move there
                y-=1
                moves +=1
            else:
                while(town[x][y-1] != 0): # when left location isn't open
                    if(town[x-1][y] == 0): # if upper location is open, move there
                        x-=1
                        moves +=1
                    else : # if upper location isn't open, move down
                        x+=1
                        moves +=1
                continue # go back to while y != dropy
    if(x != dropx): # if current x location doesn't equal x destination, access xLoc function
        x, moves = xLoc(dropx, dropy, x, y, moves) # returns x
    print("drop off location: ", x, ",", y) # prints where customer was dropped off
    print(town)
    return x, y, moves

def SearchLeft(x, y, z, moves, TotalMade):
    '''
    Taxi looks to the left to search for a customer
    '''
    if (town[x][y-1] == 2): #if left has a customer
        town[x][y-1] = 1 # pick up customer
        z+=1 # adds to customer count
        print("Taxi is at this location now,",x, y) # Print taxi's location and show it's on street
        print("pick up location", x, y-1)
        dropx = random.choice([1,6]) # customer chooses the x location to be dropped off at
        dropy = random.choice([1,5]) # customer chooses the y location to be dropped off at
        print("Expected Destination: ", dropx, ",",  dropy)
        distance = abs((dropx - x)) + abs((dropy - y)) # calculates distance from current location to drop-off location
        print("Distance to destination: ", distance)
        cost = distance * 1 # Price for ride is the distance multiplied by 1
        print("Cost for ride is: $", cost)
        TotalMade +=cost # Calculates Total Money Made by adding each price
        x, y, moves = GPS(dropx, dropy, x, y, moves) # taxi navigates to destination and drops off customer
    return x, y, moves, TotalMade
        
def SearchRight(x, y, z, moves, TotalMade):
    '''
    Taxi looks to the right to search for a customer
    '''
    if (town[x][y+1] == 2): #if right has a customer
        town[x][y+1] = 1 # pick up customer
        z+=1 # adds to customer count
        print("Taxi is at this location now,",x, y) # Print taxi's location and show it's on street
        print("pick up location", x, y+1)
        dropx = random.choice([1,6]) # customer chooses the x location to be dropped off at
        dropy = random.choice([1,5]) # customer chooses the y location to be dropped off at
        print("Expected Destination: ", dropx, ",",  dropy)
        distance = abs((dropx - x)) + abs((dropy - y)) # calculates distance from current location to drop-off location
        print("Distance to destination: ", distance)
        cost = distance * 1 # Price for ride is the distance multiplied by 1
        print("Cost for ride is: $", cost)
        TotalMade +=cost # Calculates Total Money Made by adding each price
        x, y, moves = GPS(dropx, dropy, x, y, moves) # taxi navigates to destination and drops off customer
    return x, y, moves, TotalMade
        
def SearchAbove(x, y, z, moves, TotalMade):
    '''
    Taxi looks up to search for a customer
    '''
    if (town[x+1][y] == 2): #if above has a customer
        town[x+1][y] = 1 # pick up customer
        z+=1 # adds to customer count
        print("Taxi is at this location now,",x, y) # Print taxi's location and show it's on street
        print("pick up location", x, y+1)
        dropx = random.choice([1,6]) # customer chooses the x location to be dropped off at
        dropy = random.choice([1,5]) # customer chooses the y location to be dropped off at
        print("Expected Destination: ", dropx, ",",  dropy)
        distance = abs((dropx - x)) + abs((dropy - y)) # calculates distance from current location to drop-off location
        print("Distance to destination: ", distance)
        cost = distance * 1 # Price for ride is the distance multiplied by 1
        print("Cost for ride is: $", cost)
        TotalMade +=cost # Calculates Total Money Made by adding each price
        x, y, moves = GPS(dropx, dropy, x, y, moves) # taxi navigates to destination and drops off customer
    return x, y, moves, TotalMade
        
def SearchBelow(x, y, z, moves, TotalMade):
    '''
    Taxi looks down to search for a customer
    '''
    if (town[x-1][y] == 2): #if below has a customer
        town[x-1][y] = 1 # pick up customer
        z+=1 # adds to customer count
        print("Taxi is at this location now,",x, y) # Print taxi's location and show it's on street
        print("pick up location", x, y+1)
        dropx = random.choice([1,6]) # customer chooses the x location to be dropped off at
        dropy = random.choice([1,5]) # customer chooses the y location to be dropped off at
        print("Expected Destination: ", dropx, ",",  dropy)
        distance = abs((dropx - x)) + abs((dropy - y)) # calculates distance from current location to drop-off location
        print("Distance to destination: ", distance)
        cost = distance * 1 # Price for ride is the distance multiplied by 1
        print("Cost for ride is: $", cost)
        TotalMade +=cost # Calculates Total Money Made by adding each price
        x, y, moves = GPS(dropx, dropy, x, y, moves) # taxi navigates to destination and drops off customer
    return x, y, moves, TotalMade
  


# In[3]:


TotalMade= 0
moves = 0
print("Taxi starts at: ", x, y)
roundMoves = 15
previousMoves = 0
while moves<=300: # Taxi shift ends after 120 minutes
    
    rounds = 0
    if roundMoves>=15: # New customers every 15 minutes
        roundMoves = 0
        # 0 = street, 1 = land/houses, 2 = potential customer
        town = [
            [1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]
            ]
    
    
        random_num = 0
        randCustomers = random.randrange(2,6) # 2-5 customers can appear at a time
        for k in range(randCustomers): # customers appear in town
            random_num = 0
            while(random_num != 1):
                i = random.randrange(7)
                rand_idx = random.randrange(len(town[i]))
                random_num = town[i][rand_idx]

            town[i][rand_idx] = 2
        print("New Customers") # New customers not visible to driver unless driven the the customers position
        print(town)
        
        rounds+=1
    if (moves > 0):
        print("drive around again")
    x, y, moves, TotalMade= SearchLeft(x, y, z, moves, TotalMade)
    x, y, moves, TotalMade= SearchRight(x, y, z, moves, TotalMade)
    x, y, moves, TotalMade= SearchAbove(x, y, z, moves, TotalMade)
    x, y, moves, TotalMade= SearchBelow(x, y, z, moves, TotalMade)
    while(town[x+1][y]== 0):# moves down
        x+=1 # Taxi travels to find next customer
        moves +=1
        print("Taxi is at this location now,",x, y) # Print taxi's location
        x, y, moves, TotalMade= SearchLeft(x, y, z, moves, TotalMade)
        x, y, moves, TotalMade= SearchRight(x, y, z, moves, TotalMade)
        x, y, moves, TotalMade= SearchAbove(x, y, z, moves, TotalMade)
        x, y, moves, TotalMade= SearchBelow(x, y, z, moves, TotalMade)
    while(town[x][y-1] == 0): # move left
        y-=1
        moves +=1
        print("Taxi is at this location now,",x, y) # Print taxi's location
        x, y, moves, TotalMade= SearchLeft(x, y, z, moves, TotalMade)
        x, y, moves, TotalMade= SearchRight(x, y, z, moves, TotalMade)
        x, y, moves, TotalMade= SearchAbove(x, y, z, moves, TotalMade)
        x, y, moves, TotalMade= SearchBelow(x, y, z, moves, TotalMade)
    while(town[x-1][y]== 0): # move up
        x-=1
        moves +=1
        print("Taxi is at this location now,",x, y) # Print taxi's location
        x, y, moves, TotalMade= SearchLeft(x, y, z, moves, TotalMade)
        x, y, moves, TotalMade= SearchRight(x, y, z, moves, TotalMade)
        x, y, moves, TotalMade= SearchAbove(x, y, z, moves, TotalMade)
        x, y, moves, TotalMade= SearchBelow(x, y, z, moves, TotalMade)
        if(x == 0 and y == 1):
            x+=1
            moves +=1
            break
    while(town[x][y+1] == 0): # While the right of the taxi is the road
        y+=1 # move right
        moves +=1
        print("Taxi is at this location now,",x, y) # Print taxi's location
        x, y, moves, TotalMade= SearchLeft(x, y, z, moves, TotalMade)
        x, y, moves, TotalMade= SearchRight(x, y, z, moves, TotalMade)
        x, y, moves, TotalMade= SearchAbove(x, y, z, moves, TotalMade)
        x, y, moves, TotalMade= SearchBelow(x, y, z, moves, TotalMade)

    roundMoves = moves - previousMoves
    previousMoves = moves

    if (moves>=300):
        print("shift ended")
# 1 move = 1 minute
    


# In[4]:


print("\nShift has ended, thanks for using myTaxi!")
print("Distance Travelled:", moves, "spaces")
#Performance
print("Expected Work Time: 300 minutes")
expectedT = 300
print("Actual Work Time:", moves, "minutes")
actualT = moves
Tperformance = ((actualT-expectedT)/expectedT)*100 # calculates increase
print("Time Percentage Increase:", Tperformance, "%")

#Grades Performance for Time
if(Tperformance ==0):
    print("Perfect Performance")
elif(Tperformance<= 5):
    print("Great Performance")
elif (Tperformance>=10 and Tperformance <20):
    print("Okay performance")
elif(Tperformance >= 20):
    print("Bad Performance")
else:# between 5-10
    print("Good Performance") 

print("Expected Money Made: $ 100")
print("Total Money Made: $",TotalMade )
expectedM = 100
actualM = TotalMade
Mperformance = ((actualM-expectedM)/expectedM)*100 # calculates increase
print("Money Percentage Increase:", Mperformance, "%")
#Grades Performance for Money
if(Mperformance == 0):
    print("Perfect Performance")
elif(Mperformance> 0):
    print("Outstanding Performance")
elif (Mperformance<0 and Mperformance >= -10):
    print("Okay performance")
else:
    print("Bad Performance")
#End of Program




# ### Resources Used
# #### https://pynative.com/python-random-choice/#h-a-random-choice-from-a-2d-array
# #### https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
# #### https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
# #### https://www.w3schools.com/python/ref_random_randrange.asp
# #### https://www.skillsyouneed.com/num/percent-change.html
# #### https://stackoverflow.com/questions/51318249/python-how-do-i-replace-value-in-a-nested-list
# #### https://realpython.com/python-enumerate/#using-pythons-enumerate
# #### https://pynative.com/python-random-choice/#h-a-random-choice-from-a-2d-array
# #### Vacuum Program

# In[ ]:




