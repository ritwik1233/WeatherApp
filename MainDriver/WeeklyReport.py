import gi
from apiCalls.apicalls import getHistoricalWeatherForLocation
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from datetime import datetime
from database.dbcalls import add_report


class WeeklyReport:

    def save_data(self, button):
        humidity = []
        pressure = []
        temperatureHigh = []
        temperatureLow = []
        for key in range(len(self.alljsonDataValue)):
            for key, value in self.alljsonDataValue[key].items():
                if key == 'humidity':
                    humidity.append(value)
                if key == 'pressure':
                    pressure.append(value)
                if key == 'temperatureHigh':
                    temperatureHigh.append(value)
                if key == 'temperatureLow':
                    temperatureLow.append(value)
        allData = dict()
        allData['date'] = self.alljsonDataValue[0]['time']
        allData['location'] = self.city.get_text()
        allData['humidity'] = humidity
        allData['pressure'] = pressure
        allData['temperatureHigh'] = temperatureHigh
        allData['temperatureLow'] = temperatureLow
        result = []
        result.append(allData)
        add_report(allData)
        self.window.show_all()

    def on_historical_data_click(self, button):
        # get the city object text view
        self.city = self.builder.get_object('cityID')
        if len(self.city.get_text()) > 0:
            # call the getHistoricalWeatherForLocation function and pass the city name as parameter .
            # Store the response in a variable
            alljsonData = getHistoricalWeatherForLocation(self.city.get_text())
            # if alljsonData consists is not empty
            if len(alljsonData) > 0:
                # if the gtk.box consists of the previously searched data
                # Remove the data
                if self.weeklyReport.get_children():
                    for i in self.weeklyReport.get_children():
                        self.weeklyReport.remove(i)
                label = Gtk.Label(" Weekly Weather Report")
                self.weeklyReport.pack_start(label, True, True, 1)
                day = 1
                # get the daily data from the alljsonData
                self.alljsonDataValue = alljsonData['daily']['data']
                for k in range(len(self.alljsonDataValue)):
                    label = Gtk.Label(" Day " + str(day) + " Weather Report")
                    self.weeklyReport.pack_start(label, True, True, 1)
                    for key, value in self.alljsonDataValue[k].items():
                        # convert time from unix timestamp to actual time
                        if key == 'time' or key =='sunriseTime' or key =='precipIntensityMaxTime' or key =='sunsetTime'or key =='temperatureHighTime'or key =='temperatureLowTime'or key =='apparentTemperatureHighTime'or key =='apparentTemperatureLowTime'or key =='temperatureMinTime'or key =='temperatureMaxTime'or key =='apparentTemperatureMinTime'or key =='apparentTemperatureMaxTime' or key =='windGustTime'or key =='uvIndexTime'  :
                            value = datetime.fromtimestamp(value).strftime('%d %B %Y %H:%M:%S')
                        buffer1 = Gtk.TextBuffer()
                        buffer1.set_text(key + ' : ' + str(value))
                        textview = Gtk.TextView(buffer=buffer1)
                        self.weeklyReport.pack_start(textview, True, True, 2)
                    day = day + 1
            self.window.show_all()
            return True
        else:
            label = Gtk.Label("Location name empty ")
            self.weeklyReport.pack_start(label, True, True, 1)
            self.window.show_all()
            return False
