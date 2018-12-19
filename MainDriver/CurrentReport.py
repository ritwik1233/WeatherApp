import gi
from apiCalls.apicalls import getWeatherForLocation
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from datetime import datetime


class CurrentLocation():

    def onSearchClick(self, button):
        # get the city object text view
        self.text = self.builder.get_object('locationEntry')
        # If location text is not empty
        if len(self.text.get_text()) > 0:
            # call the getWeatherForLocation function and pass the city name as parameter .
            # Store the response in a variable
            self.json = getWeatherForLocation(self.text.get_text())
            # if alljsonData consists is not empty
            if (len(self.json) > 0):
                # if the gtk.box consists of the previously searched data
                # Remove the data
                if self.currentReport.get_children():
                    for i in self.currentReport.get_children():
                        self.box.remove(i)
                label = Gtk.Label(self.text.get_text() + " Weather Report")
                self.currentReport.pack_start(label, True, True, 1)
                buffer1 = Gtk.TextBuffer()
                buffer1.set_text('timezone : ' + str(self.json['timezone']))
                textfield = Gtk.TextView(buffer=buffer1)
                self.currentReport.pack_start(textfield, True, True, 2)
                for key, value in self.json['currently'].items():
                    # convert time from unix timestamp to actual time
                    if key == 'time':
                        value = datetime.fromtimestamp(value).strftime('%d %B %Y %H:%M:%S')
                    buffer1 = Gtk.TextBuffer()
                    buffer1.set_text(key + ' : ' + str(value))
                    textfield = Gtk.TextView(buffer=buffer1)
                    self.currentReport.pack_start(textfield, True, True, 2)
            else:
                label = Gtk.Label("Error no server response.Please check the internet connection")
                self.currentReport.pack_start(label, True, True, 1)
        else:
            label = Gtk.Label("Location name empty please type something")
            self.currentReport.pack_start(label, True, True, 1)
        self.window.show_all()
