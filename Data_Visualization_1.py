#import libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

#import database: 
cardb= pd.read_csv(r"C:\Users\lazra\OneDrive\Bureau\Data Mining project\wandaloo_cars_cleaned.csv")
print(cardb.head())
print(cardb.dtypes)

#Graph1 : Price Distribution
plt.subplot(2,2,1)
plt.hist(cardb.Price, bins=300)
plt.xlabel("Prix")
plt.ylabel("N of cars")
plt.ylim(0, 1300)
plt.xlim(0, 999000)
mean = np.mean(cardb.Price)
plt.axvline(x=mean, color='r', linestyle='--', label='Mean')
plt.text(mean, 50, f"Mean: {mean:.2f}", rotation=90, va='bottom')


#graph2 : Relation entre kilometrage et prix
plt.subplot(2,2,2)
plt.xlim(0, 300000)
plt.ylim(0, 700000)
plt.scatter(data=cardb, x='Kilométrage', y='Price')
plt.xlabel("Kilométrage")
plt.ylabel("Prix")

#graph3 : Relation entre Modèle et prix
plt.subplot(2,2,3)
plt.xlim(1985, 2022)
plt.ylim(0, 700000)
plt.scatter(data=cardb, x='Modèle', y='Price')
plt.xlabel("Modèle")
plt.ylabel("Prix")


#graph4 : Relation entre conso route et Vitesse maximale
plt.subplot(2,2,4)
plt.xlim(0, 13)
plt.ylim(140, 300)
plt.scatter(data=cardb, x='Conso. route', y='Vitesse maxi.')
plt.xlabel("Conso. route")
plt.ylabel("Vitesse maxi.")



plt.show()
