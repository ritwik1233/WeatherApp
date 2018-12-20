import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from datetime import datetime
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_gtk3agg import (FigureCanvasGTK3Agg as FigureCanvas)
from database.dbcalls import delete_report,view_report


class GraphReport:

    def on_delete_changed(self,combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            if self.graphReport.get_children():
                for i in self.graphReport.get_children():
                    self.graphReport.remove(i)
            model = combo.get_model()
            value = model[tree_iter][0]
            deleteData=dict()
            for i in range(len(self.alljson)):
                expectedtime = datetime.fromtimestamp(self.alljson[i]['date']).strftime('%d %B %Y')
                expectedtimelocation = self.alljson[i]['location']
                if expectedtime == value.split(' : ')[0].rstrip() and expectedtimelocation == value.split(' : ')[1].rstrip():
                    deleteData=self.alljson[i]

                    break
            if delete_report(deleteData):
                model = Gtk.ListStore(str)
                list = []
                self.alljson = view_report()
                for i in range(len(self.alljson)):
                    stringData = datetime.fromtimestamp(self.alljson[i]['date']).strftime('%d %B %Y ') + ' : ' + self.alljson[i]['location']
                    list.append([stringData])
                for i in range(len(list)):
                    model.append(list[i])
                self.viewDataColumn.set_model(model)
                self.deleteDataColumn.set_model(model)
                self.viewDataColumn.connect("changed", self.on_combo_changed)
                self.deleteDataColumn.connect("changed", self.on_delete_changed)
                self.window.show_all

    def on_combo_changed(self,combo):
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
                    label = Gtk.Label(expectedtimelocation + ' Graphical Report')
                    self.graphReport.pack_start(label, True, True, 2)
                    # Humidity
                    self.create_plot('Humidity', self.alljson[i]['humidity'])
                    # Pressure
                    self.create_plot('Pressure', self.alljson[i]['pressure'])
                    # Temperature
                    high = list(map(int, self.alljson[i]['temperatureHigh']))
                    low = list(map(int, self.alljson[i]['temperatureLow']))
                    temp = []
                    for k in range(len(high)):
                        temp.append(str(high[k] - low[k]))
                    self.create_plot('Temperature', temp)
                    self.window.show_all()

    def create_plot(self, yLabel, ydata):
        f = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvas(f)
        a = f.add_subplot(111)
        a.set_title(yLabel + ' Graph Report')
        a.set_xlabel('Day Number')
        a.set_ylabel(yLabel)
        t = np.arange(1, 9, 1)
        s = ydata
        a.plot(t, s)
        canvas.set_size_request(700, 500)
        self.graphReport.pack_start(canvas, True, True, 3)
