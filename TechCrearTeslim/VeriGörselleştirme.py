import pandas as pd
import matplotlib.pyplot as plt

veri = pd.read_csv("C:\\Users\\cdggt\\Desktop\\50_Startups.csv")
#1t
plt.scatter(veri["R&D Spend"], veri["Profit"], color="blue")
plt.xlabel("Arge Harcaması")
plt.ylabel("Kar")
plt.title("Arge Harcaması-Kar")
plt.show()

#2
plt.scatter(veri["Administration"],veri["Profit"], color="green")
plt.xlabel("Yönetim Harcaması")
plt.ylabel("Kar")
plt.title("Yönetim Harcaması vs Kar")
plt.show()

#3
ort_kar = veri.groupby("State")["Profit"].mean()
ort_kar.plot(kind="bar", color=["blue", "yellow", "blue"])
plt.ylabel("Ortalama Kar")
plt.title("Eyaletlere Göre Ortalama Kar")
plt.show()

#4 
veri[["R&D Spend", "Administration", "Marketing Spend"]].plot(kind="box")
plt.title("Harcama Dağılımı")
plt.ylabel("Miktarı")
plt.show()
