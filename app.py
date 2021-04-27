from flask import Flask, render_template, request
import requests
import urllib.parse
import pandas as pd
import numpy as np
import folium
import pickle
import xgboost as xgb
import os

images_folder = os.path.join('static', 'images')


app = Flask(__name__)
app.config['upload_images'] = images_folder

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')
    
@app.route('/', methods=['POST'])
def my_form_post():

    adress= ""
    try:
        calle = request.form['calle']
        altura = int(request.form['altura'])
        tipo = request.form.get('tipo')
        type_casa, type_depto, type_ph = [0, 0, 0]
        if tipo == 'casa':
            type_casa = 1
        if tipo == 'departamento':
            type_depto = 1
        if tipo == 'ph':
            type_ph = 1        
        region = 'Provincia de Buenos Aires'
        ciudad = request.form.get('ciudad')
        norte, oeste, sur, capfed = [0,0,0,0]
        if ciudad == 'norte':
            norte = 1
        if ciudad == 'oeste':
            oeste = 1
        if ciudad == 'sur':
            sur = 1
        if ciudad == 'capfed':
            capfed = 1  
            region = 'Capital Federal'      

        barrio = request.form.get('barrio')
        cubierta = float(request.form['cubierta'])
        descubierta = float(request.form['descubierta'])
        ambientes = int(request.form.get('ambientes'))
        baños = int(request.form.get('baños'))
        jardin = 0
        jardin_rta = request.form.get('jardin')
        if jardin_rta == 'on':
            jardin =1

        pileta = 0
        pileta_rta = request.form.get('pileta')
        if pileta_rta == 'on':
            pileta =1

        parrilla = 0
        parrilla_rta = request.form.get('parrilla')
        if parrilla_rta == 'on':
            parrilla =1

        terraza = 0
        terraza_rta = request.form.get('terraza')
        if terraza_rta == 'on':
            terraza =1
    
        lavadero = 0
        lavadero_rta = request.form.get('lavadero')
        if lavadero_rta == 'on':
            lavadero =1
    
        cochera = 0
        cochera_rta = request.form.get('cochera')
        if cochera_rta == 'on':
            cochera =1

        adress = str(calle) + ' ' + str(altura) + ', ' + str(barrio) + ', ' + str(region) + ', ' + 'Argentina'
        processed_adress = adress.lower()
    
        url = 'http://nominatim.openstreetmap.org/search/' + urllib.parse.quote(processed_adress) +'?format=json'
        response = requests.get(url, verify=False).json()
    
        adress_lat = float(response[0]["lat"])
        adress_lon = float(response[0]["lon"])
    
        #preparamos para predict:
        ejemplo = [adress_lat, adress_lon, ambientes, ambientes-1, baños, cubierta + descubierta, cubierta, jardin,
        cochera, parrilla, pileta, terraza, lavadero, type_casa, type_depto, type_ph, norte, oeste, sur, capfed]

        df = pd.DataFrame(columns=['lat', 'lon', 'rooms', 'bedrooms', 'bathrooms', 'surface_total',
            'surface_covered', 'jardin', 'cochera', 'parrilla', 'pileta',
            'terraza', 'lavadero', 'property_type_Casa',
            'property_type_Departamento', 'property_type_PH',
            'l2_Bs.As. G.B.A. Zona Norte', 'l2_Bs.As. G.B.A. Zona Oeste',
            'l2_Bs.As. G.B.A. Zona Sur', 'l2_Capital Federal'])
        df.loc[0] = ejemplo

        bst = xgb.Booster({"booster":"gbtree", "max_depth": 15, "eta": 0.3, "nthread":3})  # init model
        bst.load_model('ms_map/0001.model')  # load data

        predict_precio = round(int(np.exp(bst.predict(xgb.DMatrix(df)))),-3)
        
        #mapa = folium.Map(location=[adress_lat, adress_lon], zoom_start=16)
        #folium.Marker(location=[adress_lat, adress_lon], popup="Propiedad:" + adress +'. ' + 'Valuada en: US$' + str(predict_precio), icon=folium.Icon(color="red")).add_to(mapa)
        #mapa.save('ms_map/templates/mapa.html')
        
        return render_template('mapa.html', adress=adress, predict_precio=predict_precio, adress_lat= adress_lat, adress_lon= adress_lon)
    except:
        return render_template('no_answer.html')

@app.route("/map_heat", methods=["GET"])
def datavis():
    error_filename = os.path.join(app.config['upload_images'], 'error.png')
    barrio_filename = os.path.join(app.config['upload_images'], 'precio por barrio.png')
    feature_filename = os.path.join(app.config['upload_images'], 'feature import.png')
    return render_template('map_heat.html', error_image = error_filename,
    barrio_image = barrio_filename, feature_image = feature_filename
    )

if __name__ == '__main__':
    app.run(debug=True)
