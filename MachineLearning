import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def logisticRegression():
    dataset = pd.read_csv('mifem.csv')
    #replacing y|n|nk by 1|0|None
    mapping={"n":0,"y":1,"nk":None}
    dataset['stroke']=dataset['stroke'].map(mapping)
    
    Y=dataset.iloc[:,1].values
    X=dataset.iloc[:,[2,-1]].values
    
    #filling missing data
    #missing data of stroke cases
    imputer=Imputer(missing_values='NaN',strategy='most_frequent',axis=0)
    imputer.fit(X[:,[-1]])
    X[:,[-1]]=imputer.transform(X[:,[-1]])
    
    num = pd.DataFrame(X)
    
    #convert live|dead to  1|0
    label_Y=LabelEncoder()
    Y[:]=label_Y.fit_transform(Y[:])
    #split the data to trainong set and testing set
    X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=0)
    y_train = y_train.astype('int')
    #scaling the data
    from sklearn.preprocessing import StandardScaler 
    scaler_X = StandardScaler()
    X_train=scaler_X.fit_transform(X_train)
    X_test=scaler_X.transform(X_test)
    
    #fitting to the Training set 
    from sklearn.linear_model import LogisticRegression
    classifier=LogisticRegression(random_state=0)
    classifier.fit(X_train,y_train)
    
    #prediction of test results
    pred_y=classifier.predict(X_test)
    pred_y=pred_y.astype('int')
    y_test=y_test.astype('int')
    
    
    #Confusing matrix
    from sklearn.metrics import confusion_matrix
    matrix=confusion_matrix(y_test,pred_y)
    print(matrix)
    
    
    
    
if __name__=='__main__':
    logisticRegression()