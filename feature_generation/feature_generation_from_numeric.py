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
import string
import fileinput

if __name__ == '__main__':


    if (len(sys.argv)<=1): 
        data_numeric = open("../data/german.data-numeric.txt",'r')
    else:
        data_numeric_file = open(sys.argv[1],'r');  

    if (len(sys.argv)<=2):
        feature_data_prefix = "../data/features_numeric"
    else: 
        feature_data_prefix = sys.argv[2]

    if (len(sys.argv)<=3):
        random_allocation = open("../data/random_allocation_result.txt",'r')
    else: 
        random_allocation = open(sys.argv[3],'r')


    if (len(sys.argv)<=4):
        groups = 5
    else:
        groups = argv[4]

    print groups

    data_train = []
    data_test = []

    for i in range(groups):
        data_train.append(open(feature_data_prefix+'_train'+str(i)+'.txt','w'))
        data_test.append(open(feature_data_prefix+'_test'+str(i)+'.txt','w'))

    entry = data_numeric.readline()
    No = random_allocation.readline()

    while (entry):
        entry = entry.split()
        No = string.atoi(No)
        features = len(entry)-1;
        
        feature = [str(string.atoi(entry[-1])-1)]
        for i in range(features):
            feature.append(entry[i])
        
 
        feature_str = ' '.join(feature)
        for i in range(groups):
            if (i==No):
                data_test[i].write(feature_str+'\n')
            else:
                data_train[i].write(feature_str+'\n')

        entry = data_numeric.readline()
        No = random_allocation.readline()
