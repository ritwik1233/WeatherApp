import gi
from apiCalls.apicalls import getHistoricalWeatherForLocation
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from datetime import datetime


class WeeklyReport():
    def onHistoricalDataClick(self, button):
        # get the city object text view
        city = self.builder.get_object('cityID')
        if len(city.get_text()) > 0:
            # call the getHistoricalWeatherForLocation function and pass the city name as parameter .
            # Store the response in a variable
            alljsonData = getHistoricalWeatherForLocation(city.get_text())
            # if alljsonData consists is not empty
            if len(alljsonData) > 0:
                # if the gtk.box consists of the previously searched data
                # Remove the data
                if self.box1.get_children():
                    for i in self.box1.get_children():
                        self.box1.remove(i)
                label = Gtk.Label(" Weekly Weather Report")
                self.box1.pack_start(label, True, True, 1)

                day = 1
                # get the daily data from the alljsonData
                alljsonDataValue = alljsonData['daily']['data']
                for k in range(len(alljsonDataValue)):

                    label = Gtk.Label(" Day " + str(day) + " Weather Report")
                    self.box1.pack_start(label, True, True, 1)
                    for key, value in alljsonDataValue[k].items():
                        # convert time from unix timestamp to actual time
                        if key == 'time':
                            value = datetime.fromtimestamp(value).strftime('%d %B %Y %H:%M:%S')
                        buffer1 = Gtk.TextBuffer()
                        buffer1.set_text(key + ' : ' + str(value))
                        textview = Gtk.TextView(buffer=buffer1)
                        self.box1.pack_start(textview, True, True, 2)
                    day = day + 1
        else:
            label = Gtk.Label("Location name empty ")
            self.box1.pack_start(label, True, True, 1)
        self.window.show_all()