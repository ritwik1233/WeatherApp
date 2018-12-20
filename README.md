# WeatherApp

## Project Description

A Python Desktop Application where one can view daily and weekly weather reports.

## Prequisities

### Python libraries :-
* [Python GTK+ 3](https://python-gtk-3-tutorial.readthedocs.io/en/latest/)
* [matplotlib](https://matplotlib.org/contents.html)
* [requests](http://docs.python-requests.org/en/master/user/quickstart/)
* [pymongo](http://api.mongodb.com/python/current/tutorial.html)
* [numpy](http://www.numpy.org/)

### Third party API and Services :-
* [Forecast.io ](https://darksky.net/forecast/40.7127,-74.0059/us12/en).
* [Google Maps Geocode Api](https://developers.google.com/maps/documentation/geocoding/intro)
* [Mlab](https://docs.mlab.com/)

### Folder Structure

```
├── .idea
├── apiCalls       
    ├── apicalls.py      # api call to forcast.io and geocode api
├── config
    ├── config.py        # apikeys and urls for forcast.io,geocode api and mlab 
├── database
    ├── dbcalls.py       # functions to save and view data in mlab database
├── LayoutGlade             
    ├── mainWindow.glade  # glade file which contains the UI of the Application      
├── MainDriver
    ├── GraphReport.py   # UI and functionality related to getting graphical weather report 
    ├── CurrentReport.py   # UI and functionality related to getting daily weather report  
    ├── MainPage.py       # Main Driver Class
    ├── WeeklyReport.py  # UI and functionality related to getting weekly weather report
├── venv                         

```
### Project Setup

#### Forecast.io API Setup
  * Click the [link](https://darksky.net/dev) to setup and generate the api key for Forecast.io.
  * Open config.py and paste the api key in weatherappID.

#### Geocode API Setup
  * Click the [link](https://developers.google.com/maps/documentation/geocoding/intro) to setup and generate the api key for geocode api.
  * Open config.py and paste the api key in geocodeApiID.

#### Mlab Setup
  * Click the [link](https://docs.mlab.com/) to setup the mlab account and get the url.
  * Open config.py and paste the api key in mongodbURL.

### Run Instructions
#### Run on Pycharm
* Download and install [Pycharm](https://www.jetbrains.com/pycharm/)
* Open the project in pycharm
* Install all the project dependencies
* Run the MainPage.py in MainDriver python package .
