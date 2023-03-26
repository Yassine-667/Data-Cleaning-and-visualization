# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import missingno as msno
import datetime as dt


# Read in the dataset
cardb = pd.read_csv(r"C:\Users\lazra\OneDrive\Bureau\Data Mining project\wandaloo_cars.csv")


#We start analysing our Dataset
print(cardb.dtypes)
print(cardb['Price'])

# Remove "DH", "prix publique", "vendue" ,"promo"  from the price column 
cardb['Price'] = cardb['Price'].str.replace(".","", regex=False)
cardb['Price'] = cardb['Price'].str.replace("DH","", regex=False)
cardb['Price'] = cardb['Price'].str.replace("*   * Prix public","", regex=False)
cardb['Price'] = cardb['Price'].str.replace(" VENDUE","", regex=False)
cardb['Price'] = cardb['Price'].str.replace("  * promo","", regex=False)

#remove null values for the price column because it is important to have a price value ( for our model )
cardb.dropna(subset=['Price'], inplace=True)

# Convert price to float
cardb['Price'] = cardb['Price'].astype('float')

#And now we go for our next feature : Kilometrage
#remove "km" and convert our values to reel numbers ( floats)
cardb['Kilométrage'] = cardb['Kilométrage'].str.replace(".","", regex=False)
cardb['Kilométrage'] = cardb['Kilométrage'].str.replace(" km","", regex=False)
print(cardb['Kilométrage'])

#since wandaloo is a website for selling new cars ( mainly) , we will replace null values with 0 assuming they're new 
#cardb['Kilométrage'].fillna(value=0, inplace=True)
cardb['Kilométrage'] = cardb['Kilométrage'].astype('float')


#For simplicity reasons we will rename "Main" with "Première main" and then we will  replace the values with 0 and 1
cardb.rename(columns={'Main': 'Première Main'}, inplace=True)
cardb['Première Main'] = cardb['Première Main'].str.replace("Seconde","0", regex=False)
cardb['Première Main'] = cardb['Première Main'].str.replace("Première","1", regex=False)

#we will assume that the null values in "Première Main" correspond  to new cars 
cardb['Première Main'].fillna(value=1, inplace=True)
cardb['Première Main'] = cardb['Première Main'].astype('int')

#we modify the "transmision" feature 
cardb['Transmision'] = cardb['Transmision'].str.replace("Automatique","A", regex=False)
cardb['Transmision'] = cardb['Transmision'].str.replace("Manuelle","M", regex=False)


#we modify the "Puissance fiscale" feature 
cardb['Puissance fiscale'] = cardb['Puissance fiscale'].str.replace("cv","", regex=False)
cardb['Puissance fiscale'] = cardb['Puissance fiscale'].replace("-",np.nan, regex=False)
cardb['Puissance fiscale'] = cardb['Puissance fiscale'].replace("- ",np.nan, regex=False)
cardb['Puissance fiscale'] = cardb['Puissance fiscale'].replace("cv",np.nan, regex=False)
cardb['Puissance fiscale'] = cardb['Puissance fiscale'].replace("",np.nan, regex=False)
cardb['Puissance fiscale'] = cardb['Puissance fiscale'].astype('float')

#and we will also modify some of the other features

cardb['Cylindrée'] = cardb['Cylindrée'].str.strip("cm³")
cardb['Cylindrée'] = cardb['Cylindrée'].str.replace(".","", regex=False)
cardb['Cylindrée'] = cardb['Cylindrée'].astype('float')


cardb['Conso. ville'] = cardb['Conso. ville'].str.strip(" l/100 km")
cardb['Conso. ville'] = cardb['Conso. ville'].str.replace(",",".", regex=False)
cardb['Conso. ville'] = cardb['Conso. ville'].replace("-",np.nan, regex=False)
cardb['Conso. ville'] = cardb['Conso. ville'].replace("",np.nan, regex=False)
cardb.drop(cardb[cardb['Conso. ville'] == '.'].index, inplace=True)
cardb['Conso. ville'] = cardb['Conso. ville'].astype('float')


cardb['Conso. route'] = cardb['Conso. route'].str.strip(" l/100 km")
cardb['Conso. route'] = cardb['Conso. route'].str.replace(",",".", regex=False)
cardb['Conso. route'] = cardb['Conso. route'].replace("-",np.nan, regex=False)
cardb['Conso. route'] = cardb['Conso. route'].replace("",np.nan, regex=False)
cardb.drop(cardb[cardb['Conso. route'] == '.'].index, inplace=True)
cardb['Conso. route'] = cardb['Conso. route'].astype('float')


cardb['Vitesse maxi.'] = cardb['Vitesse maxi.'].str.strip(" km/h")
cardb['Vitesse maxi.'] = cardb['Vitesse maxi.'].replace("-",np.nan, regex=False)
cardb['Vitesse maxi.'] = cardb['Vitesse maxi.'].replace("",np.nan, regex=False)
cardb['Vitesse maxi.'] = cardb['Vitesse maxi.'].astype('float')


cardb['Volume du réservoir'] = cardb['Volume du réservoir'].str.strip(" litre")
cardb['Volume du réservoir'] = cardb['Volume du réservoir'].replace("-",np.nan, regex=False)
cardb['Volume du réservoir'] = cardb['Volume du réservoir'].replace("",np.nan, regex=False)
cardb['Volume du réservoir'] = cardb['Volume du réservoir'].astype('float')


cardb['Architecture'] = cardb['Architecture'].str.strip(" cylindres")
cardb['Architecture'] = cardb['Architecture'].str.strip(" cylindres en V")
cardb['Architecture'] = cardb['Architecture'].str.strip(" cylindres à plat")
cardb['Architecture'] = cardb['Architecture'].str.strip(" cylindres en ligne")
cardb['Architecture'] = cardb['Architecture'].replace("-",np.nan, regex=False)
cardb['Architecture'] = cardb['Architecture'].replace("",np.nan, regex=False)
cardb['Architecture'] = cardb['Architecture'].astype('float')

#and now lets remove duplicates
cardb = cardb.drop_duplicates()



#lets export our changes to our csv file 
cardb.to_csv(r"C:\Users\lazra\OneDrive\Bureau\Data Mining project\wandaloo_cars_cleaned.csv", index=False)

