import numpy as np
import mungetools as mg
from sklearn.linear_model import LogisticRegression

'''
Use random forrest classifier to predict Titanic survivors
Uses training data in train.csv (found in data subfolder)
predicts from test.csv
writes out to .csv in predictions subfolder
As is, this gives ~77% accuracy on test set
This can hit ~79% with some tweaking (currently overfits)
'''

# load data into pandas data frame
trdata=mg.loadData()

# get the id's for the test set
# testid = np.array(testdata.UserID)

# testdata = testdata.drop('UserID',axis=1)

# initialize classifier

model= LogisticRegression(C=20.0,penalty = 'l1',class_weight = 'auto')

model = model.fit(trdata.iloc[:,1:],trdata.iloc[:,0])

# accur = model.oob_score_

# print('Out of Bag accuracy: %f \n' %accur)


# # generate predictions
# preds = np.array(model.predict_proba(testdata))[:,1]


# # save out
# mg.writeout(preds,testid,'predictions/lrmodel_test.csv')