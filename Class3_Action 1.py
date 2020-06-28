from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# 数据加载
data = pd.read_csv('car_data.csv', encoding = "gbk")  # 导入文档中含有中文，使用gbk编码读取
train_x = data[["人均GDP", "城镇人口比重", "交通工具消费价格指数","百户拥有汽车量" ]]  # 将对应标签装入训练组


''' 没有非数字类型的feature需要转化为数字，此段代码不需要
# LabelEncoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
train_x['Gender'] = le.fit_transform(train_x['Gender'])
'''

# 规范到[0,1]空间
min_max_scaler = preprocessing.MinMaxScaler()
train_x =  min_max_scaler.fit_transform(train_x)


##使用KMeans聚类
kmeans = KMeans(n_clusters=4)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)


result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0:u'聚类结果'}, axis=1, inplace=True)
print(result)

# 手肘法
import matplotlib.pyplot as plt
sse = []
for k in range(1,11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(train_x)
    sse.append(kmeans.inertia_)
x = range(1,11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x,sse, 'o-')
plt.show()

# 使用层次聚类
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
model = AgglomerativeClustering(linkage='ward', n_clusters=3)
y = model.fit_predict(train_x)
print(y)

linkage_matrix = ward(train_x)
dendrogram(linkage_matrix)
plt.show()
