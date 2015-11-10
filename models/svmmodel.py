import sys
import math
import numpy as np
import pandas as pd
import cmd_parser as cmd
from sklearn.svm import SVC

def SelectParam(trdata,tedata,paramc=[0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],paramg=[0, 0.01, 0.05, 0.1, 0.5, 1, 1.5],split=0.7):
 
    for c in paramc:
        model=SVC(C=c,kernel = 'linear')   
        model=model.fit(trdata.iloc[:,1:],trdata.iloc[:,0])
        print str(c)+':'+str(model.score(tedata.iloc[:,1:],tedata.iloc[:,0]))+'\n'

    return

    
if __name__ == '__main__':

    num = 4

    train_data_file,test_data_file,test_result_dir = cmd.TrainTestFileParser(sys.argv,num)
    
    test_result_file = open(test_result_dir+"svm_test_result"+str(num)+".txt",'w+')

    trdata=pd.read_csv(train_data_file,header=None,sep=' ')
    tedata=pd.read_csv(test_data_file,header=None,sep=' ')

    model = SVC(C=0.4,kernel = 'linear')   

    model = model.fit(trdata.iloc[:,1:],trdata.iloc[:,0])

    accur = model.score(tedata.iloc[:,1:],tedata.iloc[:,0])

    resultClass = model.predict(tedata.iloc[:,1:])
    
    resultProba = model.decision_function(tedata.iloc[:,1:])


    print('Test data accuracy: %f\n' %(accur))  
    
    for x, y in zip(resultClass, resultProba):
        test_result_file.write(str(x)+' ')
        y = 1/(1+math.exp(y))
        test_result_file.write(str(y)+' '+str(1-y)+'\n')
             


# generate predictions
# preds = np.array(model.predict_proba(testdata))[:,-1]
# mg.writeout(preds,testid,'predictions/svmmodel_test.csv')
