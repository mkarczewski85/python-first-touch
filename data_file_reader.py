# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 09:15:38 2017

@author: Maciej
"""


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
    return storage


def print_data(storage):
    for entry in storage.data_list:
        entry.display()


def main():
    storage = map_file('mock.txt')
    print_data(storage)

if __name__ == "__main__":
    main()
