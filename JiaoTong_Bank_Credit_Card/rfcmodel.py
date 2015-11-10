import sys
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier as rfc

# load data into pandas data frame
# trdata,testdata=mg.loadData()
# trdata=mg.loadData()
# get the id's for the test set
# testid = np.array(testdata.UserID)

# testdata = testdata.drop('UserID',axis=1)

# initialize classifier 

depthlist = [3,5,10,15,20,50,100]

for i in depthlist:

	model= rfc(n_estimators=5000,oob_score=True,max_features = None, max_depth = i)

	model = model.fit(trdata.iloc[:,1:],trdata.iloc[:,0])

	accur = model.oob_score_

	print('Out of Bag accuracy: %f \n' %accur)

# generate predictions
# preds = np.array(model.predict_proba(testdata))[:,1]


# save out
# mg.writeout(preds,testid,'predictions/rfcmodel_test.csv')
