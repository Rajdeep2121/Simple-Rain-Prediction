# IMPORTING LIBRARIES
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from keras.layers import Dense
from keras.models import Sequential

# FETCHING DATA
data = pd.read_csv("rain.csv")
print(len(data))                # 25551 data points

# DATA CLEANING (removing missing values)
data.dropna(inplace=True)

# ENCODING OUTPUT 
data['RAIN'] = [1 if i==True else 0 for i in data["RAIN"]]

# DISTINGUISHING INPUT AND OUTPUT
x = data[['PRCP','TMAX','TMIN']]
y = data['RAIN']

# SPLITTING INTO TRAIN AND TEST SET
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4)

# FEATURE SCALING 
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# BUILDING THE MODEL
model  = Sequential()
model.add(Dense(units= 32, activation = 'relu', input_dim=3))
model.add(Dense(units= 16, activation = 'relu'))
model.add(Dense(units= 1, activation = 'sigmoid'))

# COMPILATION OF MODEL USING 'ADAM' OPTIMIZER
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

# TRAINING THE MODEL 
model.fit(x_train,y_train, batch_size=20, epochs=10,verbose= 1)

# SAVING THE MODEL
model.save("model.h5")

# PREDICTION 
pred = model.predict(x_test)
pred = [ 1 if y>=0.5 else 0 for y in pred]
pred_df = pd.DataFrame(pred)
print(pred_df)

# COMPUTING CONFUSION MATRIX
cm = confusion_matrix(y_test, pred)
print(cm)
