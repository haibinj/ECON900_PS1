import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn import metrics


dataset = pd.read_csv("dataset.csv",header = None)
print(dataset.head())
print(dataset.dtypes)

mean_rating = dataset[0].mean(axis = 0)
print(mean_rating)
dataset[0].fillna(mean_rating, inplace=True)

mean_avg = dataset[1].mean(axis = 0)
print(mean_avg)
dataset[1].fillna(mean_avg, inplace=True)

mean_price = dataset[2].mean(axis = 0)
print(mean_price)
dataset[2].fillna(mean_price, inplace=True)

mean_number = dataset[3].mean(axis = 0)
print(mean_number)
dataset[3].fillna(mean_number, inplace=True)

mean_year = dataset[4].mean(axis = 0)
print(mean_year)
dataset[4].fillna(mean_year, inplace=True)


print(dataset.head)

plt.scatter(dataset[0],dataset[2])
plt.savefig("scatter.png")
   #construct a machine and feed data to it.
# kmeans_machine = KMeans(n_clusters = 2).fit(dataset)

# kmeans_predictions = kmeans_machine.predict(dataset)
# 		# kmeans_machine = KMeans(n_clusters = 3).fit_predict(dataset)
# 		# this can combine the two steps into one.

# 		# use metrics
# kmeans_predictions3 = kmeans_machine.predict(dataset)

# print(metrics.silhouette_score(dataset,kmeans_predictions3))

# kmeans_machine4 = KMeans(n_clusters = 2).fit(dataset)

# kmeans_predictions4 = kmeans_machine4.predict(dataset)

# print(metrics.silhouette_score(dataset,kmeans_predictions4))
# plt.scatter(dataset[3],dataset[2],c=kmeans_predictions4)
# plt.savefig("scatter4.png")

# for i in range(4):
# 	n = i + 2
# 	print(n)
#    #construct a machine and feed data to it.
# 	kmeans_machine = KMeans(n_clusters = n).fit(dataset)
# 	kmeans_predict = kmeans_machine.predict(dataset)
# 	print(metrics.silhouette_score(dataset,kmeans_predict))
# 	plt.scatter(dataset[3],dataset[2],c=kmeans_predict)
# 	plt.savefig("scatter"+str(n)+".png")

	#====================================================
# plt.scatter(dataset[3],dataset[4],c=kmeans_predictions)

# plt.savefig("scatter_kmean3.png")
gaussian_predicitons = GaussianMixture(n_components=2).fit(dataset).predict(dataset)
print(metrics.silhouette_score(dataset,gaussian_predicitons))
# 	# the number is smaller but not meaning that this is worse than the KMean cluster.
# 	# the number is not comparable between different algorithms.

plt.scatter(dataset[0],dataset[2],c=gaussian_predicitons)

plt.savefig("scatter_gaussian.png")



# gaussian_predicitons4 = GaussianMixture(n_components=4).fit(dataset).predict(dataset)
# print(metrics.silhouette_score(dataset,gaussian_predicitons4))
# plt.scatter(dataset[3],dataset[4],c=gaussian_predicitons4)

# plt.savefig("scatter_gaussian4.png")

# for i in range(4):
# 	n = i + 2
# 	print(n)
#    #construct a machine and feed data to it.
# 	gaussian_machine = GaussianMixture(n_components = n).fit(dataset)
# 	gaussian_predict = gaussian_machine.predict(dataset)
# 	print(metrics.silhouette_score(dataset,gaussian_predict))
# 	plt.scatter(dataset[3],dataset[4],c=gaussian_predict)
# 	plt.savefig("scatter"+str(n)+".png")
