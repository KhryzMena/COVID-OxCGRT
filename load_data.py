import csv 

def load_data(filename):
    '''
    :Purpose:
        To load data from a csv file and make it accessible as a list
        of lists pertaining to each column in each row

    :Required Parameters:
        :param filename: string input of name of csv file

    :Output:
        A list of each row as a list of each column

    :Example:
        data = load_data('mycsvfile.csv')
    '''
    try:
        mylist = []
        with open(filename, encoding='utf8') as covid:
            covid_data = csv.reader(covid, delimiter=',')
            for row in covid_data:
                mylist.append(row)
            return mylist
    except UnicodeDecodeError:
        mylist = []
        with open(filename, encoding='windows-1252') as covid:
            covid_data = csv.reader(covid, delimiter=',')
            for row in covid_data:
                mylist.append(row)
            return mylist
