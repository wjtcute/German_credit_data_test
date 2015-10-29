import numpy as np
import pandas as pd
import csv
import re
'''
Data munging tools
'''

def loadData(trainfile='data/txt2int.txt'):
    tr=pd.read_csv(trainfile)
    # test=pd.read_csv(testfile)
    return tr

def writeout(pred,testid,filename,header=["UserID","Dropout"]):
    # save out to .csv
    f = open(filename,'wb')
    csvf=csv.writer(f)
    # csvf.writerow(header)
    csvf.writerows(zip(testid,pred))
    f.close()
