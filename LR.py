#Implementation of logistic regression
#Loading of data of csv file
import pandas as pd
df1 = pd.read_csv("/content/User_Data.csv")
df1.head() #printing first 5 rows
df2 = pd.get_dummies(df1, columns=["Gender"])
df2.head()
#importing libraries
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#indexing and retieving the data
X_data = df2.iloc[:,[1,2,4,5]].values
Y_data = df1.iloc[:, 3].values
#splitting of data into train and test subtests
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size = 0.2)
#Standardization
ss = StandardScaler()
x_train_ss =ss.fit_transform(X_train)
x_test_ss = ss.fit_transform(X_test)
X_train, X_test, Y_train, Y_test = train_test_split(df1[["Age","EstimatedSalary"]], df1.Purchased, test_size = 0.2)
#training data size
X_train.size
#Model fitting
model = LogisticRegression()
model.fit(x_train_ss, Y_train)
#Model prediction
model.predict(x_test_ss)
#Probability 
model.predict_proba(x_test_ss)
#Model quality
model.score(x_test_ss, Y_test)
