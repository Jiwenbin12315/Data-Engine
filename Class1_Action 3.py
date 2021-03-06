'''Action3: 对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
  拆分problem类型 => 多个字段
Step3，数据统计
  对数据进行探索：品牌投诉总数，车型投诉总数
  哪个品牌的平均车型投诉最多
'''

#Step 1 加载数据
import pandas as pd
File=pd.read_csv('car_complain.csv')

#Step 2 数据预处理 problem数据拆分
File_pro=File['problem'].str.get_dummies(',')  # 对离散型特征进行one-hot编码 Convert categorical variable into dummy/indicator variables

#用新列替换原列
File_new=File.drop('problem',1).join(File_pro)

#Step 3 数据统计

#根据品牌投诉总数 brand
df_brand=File_new.groupby(['brand'])['id'].agg(['count']).sort_values('count',ascending=False)
print('按品牌从大到小排序',format(df_brand))

#根据车型投诉总数 model
df_model=File_new.groupby(['car_model'])['id'].agg(['count']).sort_values('count',ascending=False)
print('按车型从大到小排序',format(df_model))

# 品牌平均车型投诉排序
df_brand_model_avg=File_new.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean().sort_values('count',ascending=False)  #df[](指输出数据的结果属性名称).groupby([df[属性],df[属性])(指分类的属性，数据的限定定语，可以有多个).mean()(对于数据的计算方式——函数名称)
print('按车型的平均投诉从大到小排序',format(df_brand_model_avg))

