import pandas as pd

veri = pd.read_csv("C:\\Users\\cdggt\\Desktop\\country.csv")

nufusazalan = veri.sort_values(by="Population", ascending=False)
print("Nüfusa göre azalan :")
print(nufusazalan[["Country", "Population"]])

gdpmiktarı= veri.sort_values(by="GDP ($ per capita)", ascending=True)
print("\nKişi basına düşen milli hasılaya göre artan sıralama:")
print(gdpmiktarı[["Country", "GDP ($ per capita)"]])

insansayısı = veri[veri["Population"] > 10_000_000]
print("\nNüfusu 10 milyonun üzerinde olan ülkeler:")
print(insansayısı[["Country", "Population"]])

OkurYazarlık = veri.sort_values(by="Literacy (%)", ascending=False).head(5)
print("\nEn yüksek Okur yazarlık oranına sahip 5 ülke:")
print(OkurYazarlık[["Country", "Literacy (%)"]])

kazanc10000 = veri[veri["GDP ($ per capita)"] > 10000]
print("\nKişi basına yıllık 10.000$\'dan yüksek olan ülkeler:")
print(kazanc10000[["Country", "GDP ($ per capita)"]])

veri["Population Density"] = veri["Population"] / veri["Area (sq. mi.)"]
AlanBasıİnsan= veri.sort_values(by="Population Density", ascending=False).head(10)
print("\n1 mil kare alana en çok insan düşen 10 ülke:")
print(AlanBasıİnsan[["Country", "Population Density"]])
