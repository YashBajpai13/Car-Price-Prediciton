# Car-Price-Prediction
A deployed machine learning model for predicting price of used car.

## 1.) Data Collection
The dataset used can be found on KAGGLE , link : https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho .

## 2.) Data Manipulation and Analysis
Data manipulation and analysis was done by using packages like pandas, matplotlib, seaborn etc.

## 3.) Model Creation
I chose a Random Forest Regressor model and then performed hyperparameter tuning on it using Randomized Search CV.
The adjusted r-squared score was around 0.95 .

## 4.) API
I created an API using Flask, and made a basic HTML webpage so that we can make predictions later by using the deployed webpage which can be found here : 

## 5.) Deployment
The model was deployed on heroku.
Heroku provides a free plan where you can deploy your projects for about 500+ dyno hours.
A dyno is an instance of our app that is run on the cloud.