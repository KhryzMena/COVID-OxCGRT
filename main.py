import load_data as ld
import CSVFileMaker as cfm
import columnPlot as cp
from countries import countries_dict, countries

# Runs the CSVFIleMaker program that creates separate CSV files for each country and their regions 
# separately

#cfm.countryCSVFileMaker("OxCGRT_compact_national_v1.csv")

# Define a dictionary that contains the countries and their respective regions

# Create plots for the specific column over time

columnName = "ConfirmedDeaths"

for country in countries:
    country_region_csvfilename = country.replace(" ","") + "/" + country.replace(" ","") + "OxCGRT_compact_national_v1.csv"
    country_region_pngfilename = country.replace(" ","") + "/" + country.replace(" ","") + columnName  + "OxCGRT_compact_national_v1.png"
    cp.columnPlot(country_region_csvfilename, country, columnName, country_region_pngfilename)
