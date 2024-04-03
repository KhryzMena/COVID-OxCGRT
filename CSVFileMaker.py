import csv
import os
import copy
import columnPlot as cp
import load_data as ld

def countryCSVFileMaker(csvfilename):
    '''
    :Purpose:
        To create csv files of each region within each country in the 
        given larger csv dataset

    :Required Parameters:
        :param csvfilename: String input of csv file name containing 
            csv dataset

    :Output:
        Saved csv files of each region within each country

    :Example:
        countryCSVFileMaker("OxCGRT_compact_national_v1.csv")
    '''
    csvfilename_dir = csvfilename.split(".")[0]
    try:
        os.mkdir(csvfilename_dir)
    except Exception:
        pass
    with open(csvfilename, encoding="utf8") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        dataset = []
        for row in data:
            dataset.append(row)
            
        countries_list=[]
        for row in dataset:
            if row[0]=="CountryName":
                pass
            elif row[0] not in countries_list:
                countries_list.append(row[0])
        
        # Cycle through countries listed in dataset        
        for country in countries_list:
            csv_list=[]
            csv_list.append(dataset[0]) # Append first row containing column names
            countrycsvfilename = country.replace(" ","") + csvfilename
            # Attempts to make new directory with the country as the directory
            # name. If it already exists: pass
            try:
                os.mkdir(csvfilename_dir + '/' + country.replace(" ",""))
            except Exception:
                pass
            for row in dataset:
                # Append rows containing information pertaining only the country in current cycle
                if row[0] == country:
                    csv_list.append(row)
            # Create csv file with all country data
            with open(csvfilename_dir + '/' + country.replace(" ","") + '/' + countrycsvfilename, "w", newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(csv_list)

            countrycsvfilename = csvfilename_dir + '/' + country.replace(" ","") + "/" + country.replace(" ","") + csvfilename
            us_list = ld.load_data(countrycsvfilename)
            # Create a list of regions in country in current cycle
            regions_list=[]
            for row in us_list:
                if row[2]=="RegionName":
                    pass
                elif row[2] not in regions_list:
                    regions_list.append(row[2])
            country_dataset = []
            with open(countrycsvfilename) as countrycsvfile:
                country_data = csv.reader(countrycsvfile, delimiter=",")
                for row in country_data:
                    country_dataset.append(row)
            # Create csv file for regions in country in current cycle
            for region in regions_list:
                region_dataset = []
                region_dataset.append(dataset[0])
                country_region_csvfilename = csvfilename_dir + '/' + country.replace(" ","") + "/" + country.replace(" ","") + region.replace(" ","") + csvfilename
                for row in country_dataset:
                    if row[2] == "RegionName":
                        pass
                    elif row[2] == region:
                        region_dataset.append(row)
                with open(country_region_csvfilename, "w", newline="") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerows(region_dataset)
