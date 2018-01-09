import pandas as pd
import matplotlib.pyplot as plt
import sys

#create dataframe from csv
df=pd.read_csv('GenderRatioInstitutes2012-13.csv',encoding='latin1', header=None, names=['Institutions', 'All', 'SC', 'ST', 'OBC', 'PWD', 'Muslim', 'Other Monrities', 'Foreign Students'])
plotMap=[]

combinedList = []
#create a list of lists where each list will have a corresponding box plot

colNames = ['All', 'SC', 'ST', 'OBC', 'PWD', 'Muslim', 'Other Monrities', 'Foreign Students']
for cat in colNames:
    combinedList.append([float(i) for i in df[cat].dropna().tolist() if 'Category' not in i and 'NA' not in i and float(i)<4 ])



#plotting
plt.boxplot(combinedList)

#specifying labels
plt.xticks([i for i in range(1,len(colNames)+1)],colNames)
plt.xlabel("Different Groups")
plt.ylabel("Distribution of Gender Ratio in different institutes")


plt.legend()
plt.show()
