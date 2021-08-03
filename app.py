from flask import Flask, request, render_template
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('prediction.pkl', 'rb'))


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        fuel_Diesel = 0
        fuel_LPG = 0
        fuel_Petrol = 0
        seller_type_Individual = 0
        seller_type_Trustmark_Dealer = 0
        transmission_Manual = 0
        owner_Fourth_above = 0
        owner_Second = 0
        owner_Test_car = 0
        owner_Third = 0
        try :
            km_driven = int(request.form['km_driven'])
            mileage = float(request.form['mileage'])
            engine = int(request.form['engine'])
            max_power = int(request.form['max_power'])
            seats = int(request.form['seats'])
            Car_age = float(request.form['seats'])
        except :
            return render_template('index.html', result = 'Invalid')
        seller_type = request.form['seller_type']
        transmission = request.form['transmission']
        fuel = request.form['fuel']
        owner = request.form['owner']
        if fuel == 'Petrol':
            fuel_Petrol = 1
        elif fuel == 'LPG':
            fuel_LPG = 1
        elif fuel == 'Diesel' :
            fuel_Diesel = 1
        if transmission == 'Manual':
            transmission_Manual = 1
        if owner == 'Second Owner':
            owner_Second = 1
        elif owner == 'Third Owner':
            owner_Third = 1
        elif owner == 'Test Drive Car':
            owner_Test_car = 1
        if seller_type == 'Individual':
            seller_type_Individual = 1
        elif seller_type == 'Trustmark Dealer':
            seller_type_Trustmark_Dealer = 1
        if km_driven !=0 or mileage !=0 or engine!=0 or max_power!=0 or seats!=0:
            prediction = model.predict([[km_driven, mileage, engine, max_power, seats, Car_age, fuel_Diesel, fuel_LPG, fuel_Petrol, seller_type_Individual, seller_type_Trustmark_Dealer, transmission_Manual, owner_Fourth_above, owner_Second, owner_Test_car, owner_Third]])
            output = round(prediction[0],2)
            return render_template('index.html', result ='Rs.' + str(output))
        else :
            return render_template('index.html', result = 'Invalid')
if __name__ == "__main__":
    app.run(debug = True)
