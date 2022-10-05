import pandas as pd

# loading the csv file and printing it
# df = pd.read_csv('pokemon_data.csv');

# loading the EXCEL file and printing it is almost same
# df = pd.read_excel('pokemon_data.csv'); print(df)

print(pd.read_csv('pokemon2.csv', chunksize=5))