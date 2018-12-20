import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from MainDriver.CurrentReport import CurrentLocation
from MainDriver.WeeklyReport import WeeklyReport
from database.dbcalls import view_report
from datetime import datetime
from MainDriver.GraphReport import GraphReport


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

class MainWindow:
    def on_delete_changed(self,combo):
        GraphReport.on_delete_changed(self, combo)

    def create_plot(self,yLabel,ydata):
        GraphReport.create_plot(self,yLabel,ydata)

    def on_combo_changed(self,combo):
        GraphReport.on_combo_changed(self,combo)

    def onSwitchTab(self,notebook,tab,index):
        if index == 0:
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
            self.alljson=view_report()
            self.viewDataColumn=self.builder.get_object('viewDataColumn')
            self.deleteDataColumn = self.builder.get_object('deleteDataColumn')
            model=Gtk.ListStore(str)
            list=[]
            for i in range(len(self.alljson)):
                stringData=datetime.fromtimestamp(self.alljson[i]['date']).strftime('%d %B %Y ')+' : '+self.alljson[i]['location']
                list.append([stringData])
            for i in range(len(list)):
                model.append(list[i])
            self.viewDataColumn.set_model(model)
            self.deleteDataColumn.set_model(model)
            self.viewDataColumn.connect("changed", self.on_combo_changed)
            self.deleteDataColumn.connect("changed", self.on_delete_changed)

            self.window.show_all

    def save_data(self,button):
        WeeklyReport.save_data(self,button)

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
        self.searchButton.connect("clicked", self.on_search_click)
        #Search Historical Data
        self.searchHistoryButton = self.builder.get_object('searchHistory')
        self.searchHistoryButton.connect("clicked", self.on_historical_data_click)
        # GraphicalReport
        self.graphReport=self.builder.get_object('GraphicalReport')
        # show the window
        self.window.show_all()
        # create the window
        Gtk.main()

    def on_search_click(self,button):
        CurrentLocation.on_search_click(self,button)

    def on_historical_data_click(self,button):

        if WeeklyReport.on_historical_data_click(self,button):
            save_button = Gtk.Button.new_with_label("Save Report")
            save_button.connect("clicked", self.save_data)
            self.weeklyReport.pack_start(save_button, True, True, 2)
            self.window.show_all()


window=MainWindow()
window.__init__()