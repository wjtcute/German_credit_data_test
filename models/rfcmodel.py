import sys
import numpy as np
import pandas as pd
import cmd_parser as cmd
from sklearn.ensemble import RandomForestClassifier as rfc

# load data into pandas data frame
# trdata,testdata=mg.loadData()
# trdata=mg.loadData()
# get the id's for the test set
# testid = np.array(testdata.UserID)

# testdata = testdata.drop('UserID',axis=1)

# initialize classifier 

if __name__ == '__main__':

    num = 4

    train_data_file,test_data_file,test_result_dir = cmd.TrainTestFileParser(sys.argv,num)
    
    test_result_file = open(test_result_dir+"rfc_test_result"+str(num)+".txt",'w+')

    trdata=pd.read_csv(train_data_file,header=None,sep=' ')
    tedata=pd.read_csv(test_data_file,header=None,sep=' ')

    #depthlist = [5,10,15,20,50,100]
    model= rfc(n_estimators=5000,oob_score=True,max_features = None, max_depth = 10)
    model = model.fit(trdata.iloc[:,1:],trdata.iloc[:,0])
    accur = model.score(tedata.iloc[:,1:],tedata.iloc[:,0])
    resultClass = model.predict(tedata.iloc[:,1:])
    #resultLogProba = model.predict_log_proba(tedata.iloc[:,1:])
    resultProba = model.predict_proba(tedata.iloc[:,1:])

    for x, y in zip(resultClass, resultProba):
        test_result_file.write(str(x)+' ')
        for z in y:
            test_result_file.write(str(z)+' ')
        test_result_file.write('\n')
             
    print len(resultProba)
    
    print('Test data accuracy: %f\n' %accur)
    print('Out of Bag accuracy: %f \n' %model.oob_score_)


    exit()

    depthlist = [10]

    for i in depthlist:

        model= rfc(n_estimators=5000,oob_score=False,max_features = None, max_depth = i)
        model = model.fit(trdata.iloc[:,1:],trdata.iloc[:,0])
        #accur = model.oob_score_

    
        print('Out of Bag accuracy: %f \n' %accur)

# generate predictions
# preds = np.array(model.predict_proba(testdata))[:,1]


# save out
# mg.writeout(preds,testid,'predictions/rfcmodel_test.csv')
