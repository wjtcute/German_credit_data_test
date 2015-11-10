#-------------------------------------------------------------------------------
# Name:        feature_generation_from_numeric
# Purpose:     Generate cross validation data as train:test = 4:1 from german.data-numeric.txt
#
# Author:      WangJuntao
#
# Created:     19/06/2015
# Copyright:   (c) WangJuntao 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys
import fileinput
import random

def RandomAllocate(total):
    a = range(total)
    for i in range(total):
        j = random.randint(0,total-1);
        a[i],a[j] = a[j],a[i]
    return a
    

if __name__ == '__main__':

    if (len(sys.argv)<=1):
        total = input('The total number of items:')
    else:
        total = argv[1]

    if (len(sys.argv)<=2):
        groups = 5
    else:
        groups = argv[2]

    a = RandomAllocate(total)

    fout = open("../data/random_allocation_result.txt","w+")
    
    b = [0]*groups
    for i in range(total):
        fout.write(str(a[i]%groups)+'\n')
        b[a[i]%groups]+=1

    print b

    fout.close()

