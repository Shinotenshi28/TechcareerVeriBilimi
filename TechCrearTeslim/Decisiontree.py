import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import numpy as np

veri = pd.read_csv("C:\\Users\\cdggt\\Desktop\\dava_sonuclari.csv")

np.random.seed(13)
veri["Outcome"] = np.random.choice([0, 1], size=len(veri), p=[0.8, 0.2])

X = veri[["Case Type",
          "Case Duration (Days)",
          "Judge Experience (Years)",
          "Number of Witnesses",
          "Legal Fees (USD)",
          "Plaintiff's Reputation",
          "Defendant's Wealth (USD)",
          "Number of Evidence Items",
          "Number of Legal Precedents",
          "Settlement Offered (USD)",
          "Severity"]]

y = veri["Outcome"]

X = pd.get_dummies(X, columns=["Case Type"], drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=13, stratify=y
)

model = DecisionTreeClassifier(
    max_depth=5,
    random_state=13,
    class_weight="balanced"
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Tahmin edilen sınıflar:\n", pd.Series(y_pred).value_counts())

print("1. Accuracy :", accuracy_score(y_test, y_pred))
print("2. Precision:", precision_score(y_test, y_pred, average="weighted", zero_division=0))
print("3. Recall   :", recall_score(y_test, y_pred, average="weighted", zero_division=0))
print("4. F1-Score :", f1_score(y_test, y_pred, average="weighted", zero_division=0))

plt.figure(figsize=(27,15))
plot_tree(model, 
          feature_names=X.columns, 
          class_names=[str(c) for c in model.classes_], 
          filled=True, 
          rounded=True)
plt.show()
