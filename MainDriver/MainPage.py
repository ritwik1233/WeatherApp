import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from MainDriver.CurrentReport import CurrentLocation
from MainDriver.WeeklyReport import WeeklyReport
from database.dbcalls import addReport,viewReport
from datetime import datetime
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_gtk3agg import (FigureCanvasGTK3Agg as FigureCanvas)
class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
class MainWindow():
    def onComboChanged(self,combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            if self.graphReport.get_children():
                for i in self.graphReport.get_children():
                    self.graphReport.remove(i)
            model = combo.get_model()
            value = model[tree_iter][0]
            for i in range(len(self.alljson)):
                expectedtime = datetime.fromtimestamp(self.alljson[i]['date']).strftime('%d %B %Y')
                expectedtimelocation = self.alljson[i]['location']
                if expectedtime == value.split(' : ')[0].rstrip() and expectedtimelocation == value.split(' : ')[1].rstrip():
                     label=Gtk.Label(expectedtimelocation)

                     self.graphReport.pack_start(label,True,True,2)
                     # Humidity
                     f = Figure(figsize=(5, 4), dpi=100)
                     canvas = FigureCanvas(f)
                     a = f.add_subplot(111)
                     a.set_title('Humidity  Graph Report')
                     a.set_xlabel('Day Number')
                     a.set_ylabel('humidity')
                     t = np.arange(1, 9, 1)
                     humidity=[i * 100 for i in self.alljson[i]['humidity']]
                     s = humidity
                     a.plot(t, s)
                     canvas.set_size_request(500, 500)
                     self.graphReport.pack_start(canvas, True, True, 3)
                     self.window.show_all()

    def onSwitchTab(self,notebook,tab,index):
        if index== 0:
            if self.weeklyReport.get_children():
                for i in self.weeklyReport.get_children():
                    self.weeklyReport.remove(i)
            if self.graphReport.get_children():
                for i in self.graphReport.get_children():
                    self.graphReport.remove(i)
        if index == 1:
            if self.currentReport.get_children():
                for i in self.currentReport.get_children():
                    self.currentReport.remove(i)
            if self.graphReport.get_children():
                for i in self.graphReport.get_children():
                    self.graphReport.remove(i)
        if index == 2:
            if self.weeklyReport.get_children():
                for i in self.weeklyReport.get_children():
                    self.weeklyReport.remove(i)
            if self.currentReport.get_children():
                for i in self.currentReport.get_children():
                    self.currentReport.remove(i)
            self.alljson=viewReport()
            self.viewDataColumn=self.builder.get_object('viewDataColumn')
            model=Gtk.ListStore(str)
            list=[]
            for i in range(len(self.alljson)):
                stringData=datetime.fromtimestamp(self.alljson[i]['date']).strftime('%d %B %Y ')+' : '+self.alljson[i]['location']
                list.append([stringData])
            for i in range(len(list)):
                model.append(list[i])
            self.viewDataColumn.set_model(model)
            self.viewDataColumn.connect("changed", self.onComboChanged)
            self.window.show_all
    def save_Data(self,button):
        humidity=[]
        pressure=[]
        temperatureHigh=[]
        temperatureLow=[]
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
        allData=dict()
        allData['date'] = self.alljsonDataValue[0]['time']
        allData['location']=self.city.get_text()
        allData['humidity'] = humidity
        allData['pressure'] = pressure
        allData['temperatureHigh'] = temperatureHigh
        allData['temperatureLow'] = temperatureLow
        result=[]
        result.append(allData)
        addReport(allData)
        self.window.show_all()

    def __init__(self):
        # Get mainwindow  glade file in directory
        mainWindowDirectory = os.path.normpath(os.getcwd() + os.sep + os.pardir) + '//LayoutGlade'
        # Create a builder
        self.builder = Gtk.Builder()
        # add  builder
        self.builder.add_from_file(mainWindowDirectory + "//mainWindow.glade")
        # connect the builder to
        self.builder.connect_signals(Handler())
        # get the window from the builder
        self.window = self.builder.get_object("window1")
        # set the default size of the builder
        self.window.set_size_request(800, 500)
        # get note book
        self.notebook = self.builder.get_object('notebook1')
        self.notebook.connect('switch-page', self.onSwitchTab)
         # get the box ID for editData box
        self.currentReport = self.builder.get_object('editData')
        # get the box ID for editData box
        self.weeklyReport = self.builder.get_object('editHistory')
        ##Search cuurent data
        ## get search Button
        self.searchButton=self.builder.get_object('search')
        self.searchButton.connect("clicked", self.onSearchClick)
        ##Search Historical Data
        self.searchHistoryButton = self.builder.get_object('searchHistory')
        self.searchHistoryButton.connect("clicked", self.onHistoricalDataClick)
        # GraphicalReport
        self.graphReport=self.builder.get_object('GraphicalReport')
        # show the window
        self.window.show_all()
        # create the window
        Gtk.main()
    def onSearchClick(self,button):
       CurrentLocation.onSearchClick(self,button)
    def onHistoricalDataClick(self,button):
        if(WeeklyReport.onHistoricalClick(self,button)):
            self.saveButton = Gtk.Button.new_with_label("Save Report")
            self.saveButton.connect("clicked", self.save_Data)
            self.weeklyReport.pack_start(self.saveButton, True, True, 2)
            self.window.show_all()


window=MainWindow()
window.__init__()