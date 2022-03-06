import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def marks_preduction(hrs):
    data = pd.read_csv('st.csv')
    data = data.fillna(data.mean())
    data.isnull().sum()
    X = data.drop(columns = 'student_marks')
    y = data.drop(columns = 'study_hours')

    from sklearn.model_selection import train_test_split
    X_train , X_test , y_train , y_test = train_test_split(X, y , random_state=51 , test_size=0.2)
    X_train.shape , y_train.shape , X_test.shape , y_test.shape

    
    model = LinearRegression()
    model.fit(X_train , y_train)
    
    X_test = np.array(hrs)
    X_test = X_test.reshape((1,-1))
    return model.predict(X_test)

