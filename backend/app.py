import pandas as pd
import json
from flask import Flask, request, jsonify
import numpy as np
import pickle
import geopandas as gpd
import geoplot as gplt
from geopandas import GeoDataFrame

app = Flask(__name__)

names=["Jahr", "Österreich", "Burgenland", "Kärnten", "Niederösterreich", "Oberösterreich", "Salzburg", "Steiermark", "Tirol", "Vorarlberg", "Wien"]

averagePrice = pd.read_excel("ergebnisse_im_ueberblick_nettomiete_und_betriebskosten_mikrozensus.xlsx", header=None, usecols = 'A:K', skiprows = 4, names=names, nrows=16)
averagePrice_json = averagePrice.to_json()

averagePricePerMeter = pd.read_excel("ergebnisse_im_ueberblick_nettomiete_und_betriebskosten_mikrozensus.xlsx", header=None, usecols = 'A:K', skiprows = 21, names=names, nrows=16)
averagePricePerMeter_json = averagePricePerMeter.to_json()

averageSpace = pd.read_excel("ergebnisse_im_ueberblick_wohnungsgroesse.xlsx", header=None, usecols = 'A:K', skiprows = 5, names=names, nrows=16)
averageSpace_json = averageSpace.to_json()

averageRooms = pd.read_excel("ergebnisse_im_ueberblick_wohnungsgroesse.xlsx", header=None, usecols = 'A:K', skiprows = 23, names=names, nrows=16)
averageRooms_json = averageRooms.to_json()

columns=["Jahr", "Insgesamt", "Hauseigentum", "Wohnungseigentum", "Gemeindewohnung", "Genossenschaftswohnung", "Andere Hauptmiete", "Sonstige"]

medianPriceLegal = pd.read_excel("ergebnisse_im_ueberblick_gesamte_wohnkosten_eu-silc.xlsx", header=None, usecols = 'A:H', skiprows = 17, names=columns, nrows=12)
medianPriceLegal_json = medianPriceLegal.to_json()

medianPriceLegalPerMeter = pd.read_excel("ergebnisse_im_ueberblick_gesamte_wohnkosten_eu-silc.xlsx", header=None, usecols = 'A:H', skiprows = 30, names=columns, nrows=12)
medianPriceLegalPerMeter_json = medianPriceLegalPerMeter.to_json()

with open('forest.pkl', 'rb') as fid:
    forest = pickle.load(fid)
    
@app.route('/averagePrice', methods=['GET'])
def averagePrice():
    return json.dumps(averagePrice_json)

@app.route('/averagePricePerMeter', methods=['GET'])
def averagePricePerMeter():
    return json.dumps(averagePricePerMeter_json)

@app.route('/averageSpace', methods=['GET'])
def averageSpace():
    return json.dumps(averageSpace_json)

@app.route('/averageRooms', methods=['GET'])
def averageRooms():
    return json.dumps(averageRooms_json)

@app.route('/medianPriceLegal', methods=['GET'])
def medianPriceLegal():
    return json.dumps(medianPriceLegal_json)

@app.route('/medianPriceLegalPerMeter', methods=['GET'])
def medianPriceLegalPerMeter():
    return json.dumps(medianPriceLegalPerMeter_json)

@app.route('/predictPrice', methods=['GET'])
def predictPrice():
    state = int(request.args.get('state'))
    size = int(request.args.get('size'))
    return json.dumps(forest.predict(np.array([[state, size]]))[0])
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)