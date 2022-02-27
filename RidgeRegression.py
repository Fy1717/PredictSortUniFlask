
# --------------- IMPORT ALL MODULES ------------------------------------------

import pandas as pd
import numpy as np
from sklearn import linear_model


# ------------------- MAIN FUNCTION -------------------------------------------

def CalculateByRidge(location, article, articleLevel, studentLevel, lessonTime):

    # --------------- GET USER'S DATA FROM INTERFACE --------------------------

    location = int(location)
    article = int(article)
    articleLevel = int(articleLevel)
    studentLevel = int(studentLevel)
    lessonTime = int(lessonTime)
    
    # --------------- GET MAIN DATA FROM CSV FILE -----------------------------

    
    
    mainData = pd.read_csv("C:/Users/furkanyildiz/Desktop/FY/FY-Home/RidgeForUniversities/Backend/data.csv")
    mainData.isnull().sum()
    mainData.drop(['BoşSütun1', 'BoşSütun2'], axis =1, inplace = True) 
    
    from sklearn.impute import SimpleImputer
    
    imputer = SimpleImputer(missing_values = np.NaN, strategy = 'mean', fill_value=None, verbose=0)
    Data = mainData.iloc[:,0:5].values
    
    imputer = imputer.fit(Data[:,0:5])
    Data[:,0:5] = imputer.transform(Data[:,0:5])
    #print(Data)
    
# --------------- MENTION FEATURES AND RESULT ATTRIBUTE -------------------
        
    features = Data[:,0:5]
    features = pd.DataFrame(data = features, index = range(19), columns=['Konum','AkademikYayinSayisi','AkademikYayinDerecesi','OgrenciSeviyesi','DersSaati'])    
    
    resultAttribute = mainData.sr

    # --------------- CALL RIDGE REGRESSION -----------------------------------

    reg = linear_model.Ridge()

    # --------------- FITTING OPERATION WITH FEATURES AND RESULT ATTRIBUTE ----

    reg.fit(features, resultAttribute)

    # --------------- PREDICT OPERATION ---------------------------------------

    testAttributes = [[location, article, articleLevel, studentLevel, lessonTime]]
    predictResult = reg.predict(testAttributes)

    return int(predictResult)
