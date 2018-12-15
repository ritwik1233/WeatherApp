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
            #Create a url variable for Google Maps Api consists of cityname and api key

            url = geoCodeURL + '?address=' + city + '&key=' + geocodeApiID

            #Send the get request and store the response in resp vatiable

            resp = requests.get(url)

            #Convert response from json to python dictionary format and store it

            jsonData = json.loads(resp.text)

            #return the result

            return jsonData['results'][0]['geometry']['location']

        except requests.exceptions.ConnectionError:
             # else return empty dictionary
            return []

# AUTHOR:Ritwik Sinha
# DATE CREATED:09/12/2018
# PURPOSE: This function is used to get the daily data from the api
# PARAMETER: city
# RETURN : return the response in form of Python dictionary
def getWeatherForLocation(city):
        try:
            # call the geoCode function which accesses the google maps api and returns the result in python dictionary format

            geocodedata=geoCode(city)

            # If dictionary length is greater than 0,means that there is a valid response
            if(len(geocodedata)>0):

                # create a url and the latitude and longitude value from the gecodedata dictionary.
                # Also exclude unnecessary data from the response by providing the parameters in the query string
                url = weatherURL + weatherappID + '/' + str(geocodedata['lat']) + ',' + str(geocodedata['lng'])+'?exclude=minutely,hourly,daily,alerts,flags'

                # send the get request and store the response in the resp variable
                resp = requests.get(url)

                # convert the json response to python dictionary and store in a variable jsonData
                jsonData = json.loads(resp.text)

                # return the json response
                return jsonData
            else:
            # else return empty dictionary
                return []
        except requests.exceptions.ConnectionError:
             # else return empty dictionary
            return []

# AUTHOR:Ritwik Sinha
# DATE CREATED:09/12/2018
# PURPOSE: This function is used to return weekly data from the api
# PARAMETER: city
# RETURN : return the response in form of Python dictionary
def getHistoricalWeatherForLocation(city):
    try:
        # call the geoCode function which accesses the google maps api and returns the result in python dictionary format
        geocodedata = geoCode(city)


        # If dictionary length is greater than 0,means that there is a valid response
        if (len(geocodedata) > 0):
            # create a url and the latitude and longitude value from the gecodedata dictionary.
            # Also exclude unnecessary data from the response by providing the parameters in the query string

            url = weatherURL + weatherappID + '/' + str(geocodedata['lat']) + ',' + str(geocodedata['lng'])+'?exclude=minutely,hourly,currently,alerts,flags'

            # send the get request and store the response in the resp variable

            resp = requests.get(url)

            # convert the json response to python dictionary and store in a variable jsonData

            jsonData = json.loads(resp.text)

            # return the json response

            return jsonData
        else:
            # else return empty dictionary
            return []
    except requests.exceptions.ConnectionError:
        # else return empty dictionary
        return []

