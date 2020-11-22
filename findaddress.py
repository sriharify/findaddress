from flask import Flask,render_template,request,make_response,jsonify
import os
from geopy.geocoders import Nominatim

#check
app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def home():
    return render_template('home.html')


@app.route('/findaddress', methods=["POST"])
def hello():
    lat = request.form['lati']
    lon = request.form['longi']
    coordinates = str(lat)+","+str(lon)
    #{"lat":"9.9397281","lon":"78.0910666"}
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.reverse(coordinates)
    address = location.raw
    address = address['address']
    key = address.keys()
    result={}
    if 'road' in  key:
        result['road'] = address['road']
    else:
        result['road'] = None
    if 'city' in key:
        result['city'] = address['city']
    else:
        result['city'] = None
    if 'suburb' in key:
        result['suburb'] = address['suburb']
    else:
        result['suburb'] = None
    if 'postcode' in key:
        result['pincode'] = address['postcode']
    else:
        result['pincode'] = None
    if 'country' in key:
        result['country'] = address['country']
    else:
        result['country'] = None
    if 'state' in key:
        result['state'] = address['state']
    else:
        result['state'] = None
    return render_template('result.html',result=result)

if __name__ == "__main__":
    app.run(debug=True)