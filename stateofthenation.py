import matplotlib.pyplot as plt
import pandas as pd

#loading and processing the data

#Part A
houseDF2= pd.read_csv("Average-prices-Property-Type-2021-05.csv")
houseDF2.head()
s =houseDF2.loc[houseDF2.Region_Name=="Sunderland"]
n = houseDF2.loc[houseDF2.Region_Name=='Newcastle upon Tyne']
filtered = pd.concat([s, n])
filtered = filtered[["Region_Name", "Detached_Average_Price", "Semi_Detached_Average_Price", "Terraced_Average_Price", "Flat_Average_Price"]]
filtered = filtered.rename(columns={"Detached_Average_Price":"Detached", "Semi_Detached_Average_Price":"Semi-Detached","Terraced_Average_Price":"Terraced","Flat_Average_Price":"Flat"})
filtered.head()
