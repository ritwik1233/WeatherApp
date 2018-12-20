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
* Install all the project dependencies.Below is the list of dependencies
    ```
    Package         Version         Latest Version
    
    PyGObject	    3.30.4	        3.30.4
    Schemer	        0.2.11	        0.2.11
    altgraph	    0.16.1	        0.16.1
    certifi	        2018.11.29	    2018.11.29
    chardet	        3.0.4	        3.0.4
    cycler	        0.10.0	        0.10.0
    future	        0.17.1	        0.17.1
    idna	        2.8	            2.8
    inflection	    0.3.1	        0.3.1
    kiwisolver	    1.0.1	        1.0.1
    macholib	    1.11	        1.11
    matplotlib	    3.0.2	        3.0.2
    numpy	        1.15.4	        1.15.4
    pefile	        2018.8.8	    2018.8.8
    pip	            18.1	        18.1
    pycairo	        1.18.0	        1.18.0
    pymongo	        3.7.2	        3.7.2
    pyparsing	    2.3.0	        2.3.0
    python-dateutil	2.7.5	        2.7.5
    requests	    2.21.0	        2.21.0
    setuptools	    40.6.2	        40.6.3
    six	            1.12.0	        1.12.0
    urllib3	        1.24.1	        1.24.1
    ```
* Run the MainPage.py in MainDriver python package .
