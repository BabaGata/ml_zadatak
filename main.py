import json
import pickle
from flask import Flask, request, jsonify, render_template
import pandas as pd
import datetime as dt

app = Flask(__name__)
## Load the model
forest_model = pickle.load(open('random_forest_model.pkl', 'rb'))
ordinal_encoder = pickle.load(open('ordinal_encoder.pkl', 'rb'))
all_cols = ['region', 'year', 'manufacturer', 'model', 'condition', 'cylinders', 'fuel', 'odometer',
            'title_status', 'transmission', 'drive', 'type', 'paint_color', 'state', 'lat', 'long', 'posting_date',
            'VIN']
low_cardinality_cols = ['condition', 'fuel', 'title_status', 'transmission', 'drive']
high_cardinality_cols = ['model', 'region', 'type', 'VIN_country', 'VIN_year', 'VIN_manufacturer', 'VIN_plant',
                         'manufacturer', 'VIN_model_engine_type', 'paint_color', 'state', 'VIN_security_code']
condition_list = ['condition__excellent', 'condition__fair', 'condition__good', 'condition__like new',
                  'condition__new', 'condition__salvage']
fuel_list = ['fuel__diesel', 'fuel__electric', 'fuel__gas', 'fuel__hybrid', 'fuel__other']
title_status_list = ['title_status__clean', 'title_status__lien', 'title_status__missing', 'title_status__parts only',
                     'title_status__rebuilt', 'title_status__salvage']
transmission_list = ['transmission__automatic', 'transmission__manual', 'transmission__other']
drive_list = ['drive__4wd', 'drive__fwd', 'drive__rwd']
ordered_cols = ['region', 'year', 'manufacturer', 'model', 'cylinders', 'odometer', 'type', 'paint_color', 'state',
                'lat', 'long', 'posting_date', 'VIN_country', 'VIN_manufacturer', 'VIN_model_engine_type',
                'VIN_security_code', 'VIN_year', 'VIN_plant', 'condition__excellent', 'condition__fair',
                'condition__good', 'condition__like new', 'condition__new', 'condition__salvage', 'fuel__diesel',
                'fuel__electric', 'fuel__gas', 'fuel__hybrid', 'fuel__other', 'title_status__clean',
                'title_status__lien', 'title_status__missing', 'title_status__parts only', 'title_status__rebuilt',
                'title_status__salvage', 'transmission__automatic', 'transmission__manual', 'transmission__other',
                'drive__4wd', 'drive__fwd', 'drive__rwd']

def one_hot_encoder(data, list, col):
    for el in list:
        if el.replace(col + '--', '') == data[col].values:
            data[el] = True
        else:
            data[el] = False
    return data


def prepare_data(data):

    data['posting_date'] = pd.to_datetime(data['posting_date'].str[0:19])
    data['posting_date'] = data['posting_date'].map(dt.datetime.toordinal)
    data.cylinders = data.cylinders.astype('Int16')
    data.year = data.year.astype('Int16')
    data.odometer = data.odometer.astype('Int32')
    data.lat = data.lat.astype('float64')
    data.long = data.long.astype('float64')
    data.posting_date = data.posting_date.astype('float64')

    data['VIN_country'] = data.VIN.str[0:1]
    data['VIN_manufacturer'] = data.VIN.str[1:3]
    data['VIN_model_engine_type'] = data.VIN.str[3:8]
    data['VIN_security_code'] = data.VIN.str[8:9]
    data['VIN_year'] = data.VIN.str[9:10]
    data['VIN_plant'] = data.VIN.str[10:11]
    data = data.drop(['VIN'], axis=1)
    data[high_cardinality_cols] = ordinal_encoder.transform(data[high_cardinality_cols])

    for col in low_cardinality_cols:
        data = one_hot_encoder(data, eval(col + '_list'), col)
        data = data.drop([col], axis=1)

    data = data[ordered_cols]
    print(data.columns)
    return data


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict_api', methods=['POST'])
def predict_api():
    json_file = jsonify(request.get_json(force=True))
    data = json.load(json_file)
    df = pd.DataFrame.from_dict([data.values()], columns=data.keys())
    df = prepare_data(df)
    output = forest_model.predict(df.iloc[0].values.reshape(1, -1))[0]
    return jsonify(output)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    df = pd.DataFrame([data.values()], columns=data.keys())
    df = prepare_data(df)
    output = forest_model.predict(df.iloc[0].values.reshape(1, -1))[0]
    return render_template("home.html", prediction_text="Predvidena cijena je {} $".format(output))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8000"))
