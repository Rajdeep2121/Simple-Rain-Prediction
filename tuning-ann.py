import pandas as pd
from sklearn.model_selection import train_test_split
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("rain.csv")

# DATA CLEANING (removing missing values)
data.dropna(inplace=True)

# ENCODING OUTPUT 
data['RAIN'] = [1 if i==True else 0 for i in data["RAIN"]]

x = data[['PRCP','TMAX','TMIN']]
y = data['RAIN']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5)


sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

def build_classifier(optimizer):
    classifier = Sequential()
    classifier.add(Dense(output_dim=6,init='uniform',activation='relu',input_dim=3))
    classifier.add(Dense(output_dim=6,init='uniform',activation='relu'))
    classifier.add(Dense(output_dim=1,init='uniform',activation='sigmoid'))
    classifier.compile(loss="binary_crossentropy",optimizer=optimizer,metrics=['accuracy'])
    return classifier


classifier = KerasClassifier(build_fn=build_classifier)
parameters = {'batch_size':[10,20],'epochs':[10,20],'optimizer':['adam','rmsprop']}

grid_search = GridSearchCV(estimator=classifier,param_grid=parameters,n_jobs=-1,verbose=1,scoring='accuracy',cv=10)
grid_search = grid_search.fit(x_train,y_train)

best_parameters = grid_search.best_params_
best_accuracy = grid_search.best_score_

print("best parameters:",best_parameters,",best accuracy:",best_accuracy)