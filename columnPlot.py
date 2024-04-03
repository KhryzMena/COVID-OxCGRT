import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime

def columnPlot(csvfilename, country, columnName, image_filename, region=''):
    '''
    :Purpose:
        To create a plot of columnName vs. Time and save it automatically
        to the appropriate country folder.

    :Required Parameters:
        :param csvfilename: requires string input of csv file name that 
            contains data to be plotted
        :param country: string input of the country of which the csv
            data file pertains to
        :param columnName: string input of column data that is to be plotted
            with time
        :param image_filename: string input for file name of output image file

    :Optional Parameters:
        :param region: string input of region within country. If country
            does not contain region data leave as is.

    :Output:
        Saved png file
            
    :Example:
        columnPlot("mycsvfile.csv", "United States", "ConfirmedCases", mycsvfile_confirmedcases.png, region="Alabama")
    '''
    dataset = []
    with open(csvfilename) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            if row != []:
                dataset.append(row)
    
    columnIndex = dataset[0].index(columnName)
    dateIndex = dataset[0].index("Date")
    
    dates_list = []
    column_list = []
    
    i = 1
    while i < len(dataset):
        dates_list.append(datetime.fromisoformat(dataset[i][dateIndex][0:4]+'-'+dataset[i][dateIndex][4:6]+'-'+dataset[i][dateIndex][6:8]))
        try:
            column_list.append(int(dataset[i][columnIndex]))
        except ValueError:
            column_list.append(None)
        i += 1
    
    plt.plot(dates_list,column_list)
    plt.xlabel('Date')
    plt.ylabel(columnName)
    plt.title(country + " " + region + " " + columnName + ' Over Time')
    plt.xticks(rotation=30)
    plt.savefig(image_filename)
    #plt.show()
    plt.close()