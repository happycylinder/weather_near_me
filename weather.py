from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

def checkCoord(lat, lon, desired):
    url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&APPID=385e616862b080819e31595909485307"
    res = requests.get(url)
    if res.json()['weather'][0]['main'].find(desired) == 0:
        resp = jsonify({"Success": "AHA! It's near these coordinates: " + str(res.json()['coord']['lat']) + "," + str(res.json()['coord']['lon'])})
        return resp

@app.route('/weather', methods=["POST"])
def weather():
    req = request.get_json()

    if not req.get('longitude') or not req.get('latitude') or not req.get('weather'):
        resp = jsonify({"Error": "Missing arguments. 'longitude', 'latitude', and 'weather' are required"})
        resp.status_code = 400
        return resp

    lon = req.get('longitude')
    lat = req.get('latitude')
    desired = req.get('weather')

    url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&APPID=385e616862b080819e31595909485307"
    res = requests.get(url)
    if res.json()['weather'][0]['main'].find(desired) == 0:
        resp = jsonify({"Success": "AHA! It's near these coordinates: " + str(res.json()['coord']['lat']) + "," + str(res.json()['coord']['lon'])})
 
        return resp

    size = .5
    latlist = []
    lonlist = []

    found = False
    while found != True:
        lat += size
        resp = checkCoord(lat, lon, desired)
        if resp:
            return resp

        latlist.append(lat)
        lonlist.append(lon)
        print "Checking...: " + str(lat) + "," + str(lon)

        lon -= size

        resp = checkCoord(lat, lon, desired)
        if resp:
            return resp        

        latlist.append(lat)
        lonlist.append(lon)
        print "Checking...: " + str(lat) + "," + str(lon)

        size += .5

        lat -= size
        
        resp = checkCoord(lat, lon, desired)
        if resp:
            return resp

        latlist.append(lat)
        lonlist.append(lon)
        print "Checking...: " + str(lat) + "," + str(lon)

        lon += size
        
        resp = checkCoord(lat, lon, desired)
        if resp:
            return resp

        latlist.append(lat)
        lonlist.append(lon)
        print "Checking...: " + str(lat) + "," + str(lon)

        size += .5


    #res = json.dumps


if __name__ == "__main__":
    app.run(port=8000)
