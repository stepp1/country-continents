#!/usr/bin/python
#-*- coding: utf-8 -*

import urllib
import os
import csv

def retrieve():
    '''Downloads .txt file to archive directory
    
    '''
    urllib.urlretrieve(url, dest)   
    
def get_data():
    '''gets data necessary from retrievd file
    
    '''
    with open(dest, 'rb') as readfile:
        for line in readfile.readlines():
            if line[0] != '#' and line[0] != '\n':
                splited = line.split('\t')
                yield splited[4], splited[8]     #country name (5th) and continent code (9th)
    
def write_data():
    '''Writes data to .csv file
    
    '''
    header = ['Country', 'Continent']
    with open ('../data/country-continents.csv', 'wb') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        for row in get_data():
            csv_writer.writerow(row)

if __name__== '__main__':
    url = 'http://download.geonames.org/export/dump/countryInfo.txt'
    dest =  '../archive/country-info.txt'
    retrieve()
    write_data()