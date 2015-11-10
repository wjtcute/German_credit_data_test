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

if __name__ == '__main__':
    file_data = open("data/credit-g.txt").readlines()

    f_out = open("data/txt2int.txt","w+")

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






            


