#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      GuoCheng
#
# Created:     19/06/2015
# Copyright:   (c) GuoCheng 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import fileinput

import matplotlib.pyplot as plt  
import numpy as np
 
if __name__ == '__main__':


    #read data
    file_data = open("data/txt2int.txt").readlines()

    #select feature
    row = 5

    data_list = []

    data_dict = {}

    for line in file_data:
        infolist = line.split(',')
        data_list.append(int(infolist[row]))

    for data in data_list:
        if int(data) in data_dict.keys():
            data_dict[int(data)] += 1
        elif int(data) not in data_dict.keys():
            data_dict[int(data)] = 1

    # print data_dict
    # print sorted(data_dict.keys())

    value = []
    count = []

    for key in sorted(data_dict.keys()):
        value.append(int(key))
        count.append(data_dict[int(key)])

    # print value
    # print count


    #line graph
    # plt.plot(value, count, 'b*')#,label=$cos(x^2)$)
    # plt.plot(value, count, 'r')
    # plt.title('Feature Distribution')
    # plt.legend()
    # plt.show()



    #hist graph

    # print data_list

    plt.figure(num=1, figsize=(8,6))
    plt.title('Plot 2', size=14)
    plt.xlabel('value', size=14)
    plt.ylabel('counts', size=14)
    data = np.asarray(data_list)
    print data
    plt.hist(data, 40)
    plt.show()
    
