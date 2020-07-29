# 使用KMeans进行聚类
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# 数据加载
data = pd.read_csv('CarPrice_Assignment.csv')
train_x = data.drop(['CarName', 'car_ID'], axis=1)

# 文字化数字转化为数字 doornumber cylindernumber
train_x['doornumber'] = train_x['doornumber'].replace("two",2)
train_x['doornumber'] = train_x['doornumber'].replace("four",4)
train_x['cylindernumber'] = train_x['cylindernumber'].replace("two",2)
train_x['cylindernumber'] = train_x['cylindernumber'].replace("three",3)
train_x['cylindernumber'] = train_x['cylindernumber'].replace("four",4)
train_x['cylindernumber'] = train_x['cylindernumber'].replace("five",5)
train_x['cylindernumber'] = train_x['cylindernumber'].replace("six",6)
train_x['cylindernumber'] = train_x['cylindernumber'].replace("eight",8)
train_x['cylindernumber'] = train_x['cylindernumber'].replace("twelve",12)

# LabelEncoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
train_x['fueltype'] = le.fit_transform(train_x['fueltype'])
train_x['aspiration'] = le.fit_transform(train_x['aspiration'])
train_x['carbody'] = le.fit_transform(train_x['carbody'])
train_x['drivewheel'] = le.fit_transform(train_x['drivewheel'])
train_x['enginelocation'] = le.fit_transform(train_x['enginelocation'])
train_x['enginetype'] = le.fit_transform(train_x['enginetype'])
train_x['fuelsystem'] = le.fit_transform(train_x['fuelsystem'])

# 规范化到 [0,1] 空间
min_max_scaler=preprocessing.MinMaxScaler()
train_x1=min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x1).to_csv('temp.csv', index=False)

### 使用KMeans聚类
kmeans = KMeans(n_clusters=7)
kmeans.fit(train_x1)
predict_y = kmeans.predict(train_x1)

# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)

# 将结果导出到CSV文件中
result.to_csv("autobrand_cluster_result.csv",index=False)

# 寻找volkswage,vw对应车型的聚类结果
bool1 = Sort_group['CarName'].str.contains('vw')
bool2 = Sort_group['CarName'].str.contains('volkswagen')
bool3 = Sort_group['CarName'].str.contains('vokswagen')

Sort_vw = Sort_group[bool1].append(Sort_group[bool2]).append(Sort_group[bool3])
# 聚类结果去重，转为数组
Sort_index = Sort_vw.drop_duplicates(['聚类结果'])['聚类结果'].tolist()
# 得到一个去除volkswagen的Dataframe
result_wo_vw = result.append(Sort_vw).drop_duplicates(keep=False)


# 利用聚类结果，将竞争车型列出
Sort_vw_result = result_wo_vw[result_wo_vw["聚类结果"].isin(Sort_index)]
Sort_vw_result.to_csv("Competitor_cluster_result.csv", index=False)