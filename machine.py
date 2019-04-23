import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn import metrics


dataset = pd.read_csv("games_clean.csv",header = None)
dataset = dataset.iloc[1:]
print(dataset.head())
print(dataset.dtypes)


print(dataset.head)

plt.scatter(dataset[0],dataset[2])
plt.savefig("graph_11.png")

gaussian_predicitons = GaussianMixture(n_components=8).fit(dataset).predict(dataset)
print(metrics.silhouette_score(dataset,gaussian_predicitons))


plt.scatter(dataset[0],dataset[2],c=gaussian_predicitons)

plt.savefig("scatter_gaussian8.png")