import load_data as ld
import CSVFileMaker as cfm
import columnPlot as cp
from countries import countries_dict, countries

# Runs the CSVFIleMaker program that creates separate CSV files for each country and their regions 
# separately
csvfilename = "OxCGRT_compact_subnational_v1.csv"
csvfilename_dir = csvfilename.split(".")[0]

#cfm.countryCSVFileMaker(csvfilename)

# Define a dictionary that contains the countries and their respective regions

# Create plots for the specific column over time

columnNames = ["ConfirmedCases", "ConfirmedDeaths"]

for columnName in columnNames:
    for country in countries_dict.keys():
        for region in countries_dict[country]:
            country_region_csvfilename = csvfilename_dir + '/' + country.replace(" ","") + "/" + country.replace(" ","") + region.replace(" ","") + csvfilename
            country_region_pngfilename = csvfilename_dir + '/' + country.replace(" ","") + "/" + country.replace(" ","") + region.replace(" ","") + columnName + csvfilename.split(".")[0] + ".png"
            cp.columnPlot(country_region_csvfilename, country, columnName, country_region_pngfilename, region)

