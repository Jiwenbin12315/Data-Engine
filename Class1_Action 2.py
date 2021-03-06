# Action2: 统计全班的成绩 班里有5名同学，现在需要你用Python来统计下 这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
import numpy as np
persontype = np.dtype({'names':['name', 'chinese', 'math', 'english'],'formats':['U32', 'i', 'i', 'i']})
peoples=np.array([("张飞",68,65,30),("关羽",95,76,98),("刘备",98,86,88),("典韦",90,88,77),("许褚",80,90,90)],dtype=persontype)
chineses=peoples['chinese']
maths=peoples['math']
englishs=peoples['english']
Grade=[chineses,maths,englishs]

print("语文的平均/最小/最大/方差/标准差的成绩为%.2f/%.2f/%.2f/%.2f/%.2f" %(np.mean(Grade[0]),np.min(Grade[0]),np.max(Grade[0]),np.var(Grade[0]),np.std(Grade[0])))
print("数学的平均/最小/最大/方差/标准差的成绩为%.2f/%.2f/%.2f/%.2f/%.2f" %(np.mean(Grade[1]),np.min(Grade[1]),np.max(Grade[1]),np.var(Grade[1]),np.std(Grade[1])))
print("英语的平均/最小/最大/方差/标准差的成绩为%.2f/%.2f/%.2f/%.2f/%.2f" %(np.mean(Grade[2]),np.min(Grade[2]),np.max(Grade[2]),np.var(Grade[2]),np.std(Grade[2])))

Score=chineses+maths+englishs

Sort_Index=np.argsort(-Score)   #argsort()函数是将x中的元素从小到大排列，提取其对应的index(索引)，然后输出||当num<0时，np.argsort()[num]就是把数组y的元素反向输出
Score_HTL=peoples['name'][Sort_Index]
Score_LTH=Score_HTL[::-1]  # 使用切分器倒序输出

print('总分从高到低：',Score_HTL)
print('总分从低到高：',Score_LTH)
