import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

veri = pd.read_csv("C:\\Users\\cdggt\\Desktop\\dava.csv")

X = veri[["Case Duration (Days)",
          "Number of Witnesses",
          "Legal Fees (USD)",
          "Number of Evidence Items",
          "Severity",
          "Outcome"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(K, inertia, "bo-")
plt.xlabel("Küme Sayısı")
plt.ylabel("Inertia")
plt.title("Elbow Yöntemi")
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
y_kume = kmeans.fit_predict(X_scaled)

veri["Kume"] = y_kume
print(veri.head())

plt.figure(figsize=(8,6))
plt.scatter(X_scaled[:,0], X_scaled[:,1], c=y_kume, cmap="viridis", s=50)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
            color="red", marker="X", s=200, label="Merkezler")
plt.xlabel("Dava Süresi")
plt.ylabel("Tanık Sayısı")
plt.title("K-Means Kümeleme")
plt.legend()
plt.show()