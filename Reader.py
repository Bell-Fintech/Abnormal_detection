# -*- coding:utf-8 -*-


import csv


def read():
    with open('HEC.csv', 'rt') as file:
        reader = csv.DictReader(file)
        thpDict = [thp for thp in reader]

    with open('CPU.csv', 'rt') as file:
        reader = csv.DictReader(file)
        cpuDict = [cpu for cpu in reader]
    return thpDict,cpuDict
