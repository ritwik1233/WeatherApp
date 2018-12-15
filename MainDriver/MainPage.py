import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from MainDriver.CurrentReport import CurrentLocation
from MainDriver.WeeklyReport import WeeklyReport
class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
class MainWindow():
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
        # get the box ID for editData box
        self.box = self.builder.get_object('editData')
        # get the box ID for editData box
        self.box1 = self.builder.get_object('editHistory')
        ##Search cuurent data
        ## get search Button
        self.searchButton=self.builder.get_object('search')
        self.searchButton.connect("clicked", self.onSearchClick)
        ##Search Historical Data
        self.searchHistoryButton = self.builder.get_object('searchHistory')
        self.searchHistoryButton.connect("clicked", self.onHistoricalDataClick)
        # show the window
        self.window.show_all()
        # create the window
        Gtk.main()
    def onSearchClick(self,button):
       CurrentLocation.onSearchClick(self,button)
    def onHistoricalDataClick(self,button):
        WeeklyReport.onHistoricalDataClick(self,button)

window=MainWindow()
window.__init__()