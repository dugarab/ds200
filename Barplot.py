import pandas as pd
import matplotlib.pyplot as plt
import sys

#create dataframe from csv
df=pd.read_csv('GenderRatioInstitutes2012-13.csv',encoding='latin1', header=None, names=['Institutions', 'All', 'SC', 'ST', 'OBC', 'PWD', 'Muslim', 'Other Monrities', 'Foreign Students'])

combinedList = []
#create a list of lists where each list will have a corresponding box plot

colNames = ['All', 'SC', 'ST', 'OBC', 'PWD', 'Muslim', 'Other Monrities', 'Foreign Students']

for cat in colNames:
    combinedList.append([float(i) for i in df[cat].dropna().tolist() if 'Category' not in i and 'NA' not in i and float(i)<4 ])


ind = [i for i in range(1,len(colNames)+1)]   # the x locations for the groups
width = 0.5      # the width of the bars: can also be len(x) sequence


plotList = [sum(lst)/len(lst) for lst in combinedList]
#plot bottom bar using height(of bar) values from first column of dataframe
p1 = plt.bar(ind, plotList, width, color='#23327c')

plt.xticks(ind,colNames,rotation = 45,size=8)
plt.xlabel("Different Groups")
plt.ylabel("Average gender ratio in Institutions")
plt.title('Gender Ratio for different groups')

#enable legend
plt.legend()
plt.show()
