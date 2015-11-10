import numpy as np
import mungetools as mg
from sklearn.ensemble import GradientBoostingClassifier as gbc
import cmd_parser as cmd
import sys
import pandas as pd

# load data into pandas data frame
# trdata,testdata=mg.loadData()
num = 4

train_data_file,test_data_file,test_result_dir = cmd.TrainTestFileParser(sys.argv,num)

trdata=pd.read_csv(train_data_file,header=None,sep=' ')
tedata=pd.read_csv(test_data_file,header=None,sep=' ')

# initialize classifier

params = {'n_estimators': 1000, 'max_depth': 3, 'subsample': 0.5,
          'learning_rate': 0.01, 'min_samples_leaf': 1, 'random_state': 3}

model= gbc(**params)

model = model.fit(trdata.iloc[:,1:],trdata.iloc[:,0])

acc = model.score(tedata.iloc[:,1:],tedata.iloc[:,0])

print("Accuracy: {:.4f}".format(acc))

# generate predictions
# preds = np.array(model.predict_proba(testdata))[:,1]


# save out
# mg.writeout(preds,testid,'predictions/rfcmodel_test.csv')