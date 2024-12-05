#Extracting data 2.0
import pandas as pd
file_path = r"C:\Users\ESTUDIANTE\Documents\Programming\Python\Macroeconomics assignment\pwt1001 (1).xlsx"
data = pd.read_excel(file_path, sheet_name='Data')
variable = ['rgdpe', 'ctfp', 'rnna']
countries = ['Colombia', ]
latest_data_all_countries = {}
for country in countries:
    country_data = data[data['country'] == country]
    latest_year = country_data['year'].max() #It will return the highest year from the countries' data in order to be used as an array of information
    latest_data = country_data[country_data['year'] == latest_year][variable] #It will retrieve all the data from the array

    latest_data_all_countries[country] = latest_data
    
all_countries_df = pd.concat(latest_data_all_countries).reset_index(level=1, drop=True)

output_file_path = r"C:\Users\ESTUDIANTE\Documents\Programming\Python\Macroeconomics assignment\data_extracted_practice_2.xlsx"
all_countries_df.to_excel(output_file_path, sheet_name='Latest Data')
print('Data saved to Excel file:', output_file_path)

