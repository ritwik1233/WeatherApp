import requests
from config.config import weatherappID,weatherURL,geocodeApiID,geoCodeURL
import json



# AUTHOR:Ritwik Sinha
# DATE CREATED:09/12/2018
# PURPOSE: This function is used to get the return the geocode for a city
# PARAMETER: city
# RETURN : return the response in form of Python dictionary
def geoCode(city):
        try:
            url = geoCodeURL + '?address=' + city + '&key=' + geocodeApiID
            resp = requests.get(url)
            jsonData = json.loads(resp.text)
            return jsonData['results'][0]['geometry']['location']
        except requests.exceptions.ConnectionError:
            return []

# AUTHOR:Ritwik Sinha
# DATE CREATED:09/12/2018
# PURPOSE: This function is used to get the return the response from the GET Web Service Call
# PARAMETER: city
# RETURN : return the response in form of Python dictionary
def getWeatherForLocation(city):
        try:
            geocodedata=geoCode(city)
            url = weatherURL +weatherappID+'/'+ str(geocodedata['lat'])+',' + str(geocodedata['lng'])
            resp = requests.get(url)
            jsonData = json.loads(resp.text)
            return jsonData
        except requests.exceptions.ConnectionError:
            return []

json=getWeatherForLocation('pee pee town')



print(json)
