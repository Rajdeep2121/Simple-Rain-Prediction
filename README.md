# Simple-Rain-Prediction
Rain Prediction using Artificial Neural Network

# Data

The 'csv' file basically contains 5 columns: 'Date','Precipitation','Max Temp','Min Temp','Rain'.<br>
It consists of 25551 rows of data.

# Data Cleaning

The data has missing values which are removed at an early stage. 

# Preparing Data 

The columns 'Precipitation','MaxTemp','MinTemp' are the variables on which the 'Rain' depends. So they are separated out. The output column i.e. 'Rain' is made binary(1=yes or 0=no).<br>
Then the data is splitted into training set and test set with a test set size of 0.3 times the original size i.e. 10220 data points.

# Feature Scaling 

The data is normalized using StandardScaler method.

# Architecture of the Model

> The model has an input layer of 32 nodes.
> A hidden layer with 16 nodes.
> An output layer with 1 node which produces 1 for rain and 0 for no rain.

# Compilation and Fitting 

The model is compiled using adam optimizer.<br>
The model is trained on a batch size of 20 and for 10 epochs.

# Prediction

For prediction, a threshold value of 0.5 is used. It means:<br>
> If prediction is greater than 0.5, then rain is predicted to happen.
> Otherwise there is no chance of rain according to the prediction.

<hr>

# TUNING OF NEURAL NETWORK

The accuracy of neural model varies on varying the hyperparameters(epochs,batch size,optimizer etc). Hence a bunch of these hyperparameters are tested and the final result is computed for best accuracy and printed.
<p align="center">
    <img src="Capture.PNG" width="300" height="300">
</p>