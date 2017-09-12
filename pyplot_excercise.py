# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:01:10 2017

@author: Maciej
"""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import sys

class EntryClass(object):
    def __init__(self, name, surname, gender, age, job, salary):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.job = job
        self.salary = salary

    def display(self):
        print('Name:', self.name, 'Surname:', self.surname, 'Gender:', self.gender, 'Age:', self.age,
              'Job description:', self.job, 'Salary:', self.salary)


class StorageData(object):
    data_list = None

    def __init__(self, data_list=[]):
        self.data_list = data_list

    def add_item(self, item):
        self.item = item
        if isinstance(self.item, EntryClass):
            self.data_list.append(self.item)
        else:
            print(Exception)

    def get_list(self):
        return self.data_list

    def get_item(self, index):
        if index < len(self.data_list):
            return self.data_list[index]
        else:
            return None


def map_file(filename):
    storage = StorageData()
    with open(filename, "rt", encoding="utf-8") as file:
        for line in file:
            data = line.split(',')
            tmp_entry = EntryClass(data[0], data[1], data[2], data[3], data[4], data[5])
            storage.add_item(tmp_entry)
    file.close()
    return storage

def visualize_data(data):

    salary_men = []
    salary_women = []
    for entry in data.data_list:
        if entry.gender == 'Male':
            value = entry.salary[1:]
            salary_men.append(float(value))
        elif entry.gender == 'Female':
            value = entry.salary[1:]
            salary_women.append(float(value))
            
    win = pg.GraphicsWindow()
    win.resize(800,350)
    win.setWindowTitle('Histogram')
    win.setBackground('w')
    plt1 = win.addPlot(title='Womens\'s salaries', labels={'left': 'Salaries'})
    plt2 = win.addPlot(title='Mens\'s salaries', labels={'left': 'Salaries'})
    
    y,x = np.histogram(salary_women, bins='auto')
    plt1.plot(x, y, stepMode=True, fillLevel=0, brush=(0,0,255,150), pen='r')
    y,x = np.histogram(salary_men, bins='auto')
    plt2.plot(x, y, stepMode=True, fillLevel=0, brush=(0,0,255,150), pen='r')
    
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
            
def main():
    
    
    
    storage = map_file('mock.txt')
    visualize_data(storage)


if __name__ == "__main__":
    main()    
