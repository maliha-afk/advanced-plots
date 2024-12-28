import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

IDdf=pd.read_csv("Iris Dataset.csv")

#print(IUdf.info())

plt.figure(figsize=(10,6))
sb.barplot(x="Species",y="SepalLengthCm",data=IDdf,palette="pastel")
plt.show()

plt.figure(figsize=(10,6))
sb.countplot(x="Species",data=IDdf,palette="pastel")
plt.show()

plt.figure(figsize=(10,6))
sb.boxplot(x="Species",y="SepalWidthCm",data=IDdf,palette="pastel")
plt.show()

plt.figure(figsize=(10,6))
sb.jointplot(x="SepalWidthCm",y="SepalWidthCm",data=IDdf,palette="pastel")
plt.show()

plt.figure(figsize=(10,6))
sb.distplot(IDdf.SepalWidthCm,kde=True,color="blue")
plt.show()


sb.pairplot(IDdf,palette="pastel",hue="Species")
plt.show()
