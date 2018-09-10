# generateruleset

#  This function asks for a matrix size (width,height), finds all combinations of 0/1 for that matrix 
#   and returns them all, indexed by their numerical value.


# PLEASE NOTE: A 3X3 MATRIX OF 9 CUBES RUNS FAST WITH (2^9) -> 512 COMBINATIONS. 
# A 5X5 MATRIX IS (2^25) COMBINATIONS, (2^25) -> 33,554,432 COMBINATIONS, 65,000 TIMES MORE THAN 2^9
# 25 PIXELS AT A TIME IS MAX RECOMMENDED FOR COMPUTATION TIME PURPOSES



import numpy as np
import math


# This formula lets you know each time a power of 2 is cycled for computational time estimation
# Plus it's cool

def ispoweroftwo(num):
    return ((num & (num - 1)) == 0) and num != 0


def generateruleset(width,height):
   
    
    def bin(s):
        return str(s) if s<=1 else bin(s>>1) + str(s&1)
 

    allrules = np.zeros(width*height*2**(width*height)).reshape(2**(width*height),width,height)
 
   

    for i in range(allrules.shape[0]):

        correctsize = list(bin(i)) 
        maxLen = width*height
        correctsize = [0]*(maxLen - len(correctsize))+correctsize       
                       
        for j in range(width):
            for k in range(height):
                thisrule = np.asarray(correctsize).reshape(width,height)
        allrules[i] = thisrule
        if ispoweroftwo(i) : print(i)
                
    return allrules



#fullbinaryarray = generateruleset(1,9)
#print(fullbinaryarray[412])

#fullbinaryarray = generateruleset(3,3)
#print(fullbinaryarray[412])

#fullbinaryarray = generateruleset(9,1)
#print(fullbinaryarray[412])

#fullbinaryarray = generateruleset(5,5)
#print(fullbinaryarray[1232])

#fullbinaryarray = generateruleset(3,7)
#print(fullbinaryarray[1232])

#fullbinaryarray = generateruleset(1,1)
#print(fullbinaryarray[1])