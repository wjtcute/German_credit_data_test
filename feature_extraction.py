#-------------------------------------------------------------------------------
# Name:        feature_extraction
# Purpose:
#
# Author:      WangJuntao
#
# Created:     19/06/2015
# Copyright:   (c) WangJuntao 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import string

import fileinput

if __name__ == '__main__':

    Attributes = 21 #including the tag dimension

    AttributeBranches = [4,1,5,11,1,5,5,1,5,3,1,4,1,3,3,1,4,1,2,2,1]

    AttributeInitial = [1,0,0,0,0,1,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1]

    raw_data = open("data/german.data.txt")
    feature_data = open("data/features.txt","w+")

    entry = raw_data.readline()

    while (entry):
        entry = entry.split()
        feature = []
        for i in range(Attributes):
            print i
            attrvec = [0]*AttributeBranches[i]
            if AttributeBranches[i] == 1:
                attrvec[0] = string.atoi(entry[i])
            elif i<9:
                branch = string.atoi(entry[i][2:]) - AttributeInitial[i]
                attrvec[branch] = 1
            else: 
                branch = string.atoi(entry[i][3:]) - AttributeInitial[i]
                attrvec[branch] = 1
            feature.extend(attrvec)

        print feature
	for i in range(len(feature)): feature[i] = str(feature[i])
        feature_data.write(' '.join(feature)+'\n')
	entry = raw_data.readline()

    exit()



    infoDict = {}

    DictCount = 0

    for line in file_data:
        if '@' in line:

            if '{' in line:
                infoList = line.split('{')[1][:-1].strip().split(',')
                for i in range(len(infoList)):
                    temp = infoList[i].strip().replace('}','')
                    infoList[i] = temp
            else:
                infoList = []

            infoDict[DictCount] = infoList
            

            print infoDict[DictCount]
            DictCount += 1

    print infoDict


    for line in file_data:
        if '%' not in line and '@' not in line:

            outline = ''
            infoList = line.strip().split(',')
            # print infoList
            for infocount in range(len(infoList)):
                # print infoDict[infocount]
                if len(infoDict[infocount]) > 0:
                    index = infoDict[infocount].index(infoList[infocount])
                    infoList[infocount] = index
            outline += str(infoList[-1])
            for item in infoList[:-1]:
                outline += ','+str(item)
            outline+='\n'
            print outline
            f_out.write(outline)






            


