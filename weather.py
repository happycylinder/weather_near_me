import requests
import json

def weather(lat, lon, desired):
    url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&APPID=385e616862b080819e31595909485307"
    res = requests.get(url)
    if res.json()['weather'][0]['main'].find(desired) == 0:
        print "you're livin it babyyyyyy"
        return

    size = .5
    latlist = []
    lonlist = []

    found = False
    while found != True:
        lat += size
        url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&APPID=385e616862b080819e31595909485307"
        res = requests.get(url)
        if res.json()['weather'][0]['main'].find(desired) == 0:
            print latlist
            print lonlist
            print "AHA! It's near these coordinates: " + str(res.json()['coord']['lat']) + "," + str(res.json()['coord']['lon'])
            return

        latlist.append(lat)
        lonlist.append(lon)
        print "Checking...: " + str(lat) + "," + str(lon)

        lon -= size
        url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&APPID=385e616862b080819e31595909485307"
        res = requests.get(url)
        if res.json()['weather'][0]['main'].find(desired) == 0:
            print latlist
            print lonlist
            print "AHA! It's near these coordinates: " + str(res.json()['coord']['lat']) + "," + str(res.json()['coord']['lon'])
            return

        latlist.append(lat)
        lonlist.append(lon)
        print "Checking...: " + str(lat) + "," + str(lon)

        size += .5

        lat -= size
        url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&APPID=385e616862b080819e31595909485307"
        res = requests.get(url)
        if res.json()['weather'][0]['main'].find(desired) == 0:
            print latlist
            print lonlist
            print "AHA! It's near these coordinates: " + str(res.json()['coord']['lat']) + "," + str(res.json()['coord']['lon'])
            return

        latlist.append(lat)
        lonlist.append(lon)
        print "Checking...: " + str(lat) + "," + str(lon)

        lon += size
        url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&APPID=385e616862b080819e31595909485307"
        res = requests.get(url)
        if res.json()['weather'][0]['main'].find(desired) == 0:
            print latlist
            print lonlist
            print "AHA! It's near these coordinates: " + str(res.json()['coord']['lat']) + "," + str(res.json()['coord']['lon'])
            return

        latlist.append(lat)
        lonlist.append(lon)
        print "Checking...: " + str(lat) + "," + str(lon)

        size += .5


    #res = json.dumps


if __name__ == "__main__":
    lat = input("What is your latitude?  ")
    lon = input("what is your longitude?  ")
    desired = input("desired weather keyword  ")
    weather(lat, lon, desired)
