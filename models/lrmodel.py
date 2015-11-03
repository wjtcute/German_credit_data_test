import sys
import numpy as np
import pandas as pd
import cmd_parser as cmd
from sklearn.linear_model import LogisticRegression

if __name__ == '__main__':

    num = 3

    train_data_file,test_data_file,test_result_dir = cmd.TrainTestFileParser(sys.argv,num)
    
    test_result_file = open(test_result_dir+"lr_test_result"+str(num)+".txt",'w+')

    trdata=pd.read_csv(train_data_file,header=None,sep=' ')
    tedata=pd.read_csv(test_data_file,header=None,sep=' ')

    model= LogisticRegression(C=3.0,penalty = 'l2',class_weight = 'auto')

    model = model.fit(trdata.iloc[:,1:],trdata.iloc[:,0])

    accur = model.score(tedata.iloc[:,1:],tedata.iloc[:,0])

    resultClass = model.predict(tedata.iloc[:,1:])
    
    resultProba = model.predict_proba(tedata.iloc[:,1:])

    print('Test data accuracy: %f\n' %(accur))       

    for x, y in zip(resultClass, resultProba):
        test_result_file.write(str(x)+' ')
        for z in y:
            test_result_file.write(str(z)+' ')
        test_result_file.write('\n')
             
  


# accur = model.oob_score_

# print('Out of Bag accuracy: %f \n' %accur)


# # generate predictions
# preds = np.array(model.predict_proba(testdata))[:,1]


# # save out
# mg.writeout(preds,testid,'predictions/lrmodel_test.csv')
