import pandas as pd
import matplotlib.pyplot as plt
import sys

colNames = ['State', 'Central University', 'State Public University', 'State Private University', 'Deemed University - Government', 'Deemed University - Government Aided', 'Deemed University - Private', 'Institute of National Importance', 'Instiutes under State Legislature Act', 'Central Open University', 'State Open University', 'State Private Open University', 'Others', 'Total']

#create dataframe from csv
df=pd.read_csv('GenderRatioInstitutesStates2012-13.csv',encoding='latin1', header=None, names=colNames)
plotMap=[]

combinedList = []
#create a list of lists where each list will have a corresponding box plot


gr = ([float(i) for i in df['Total'].dropna().tolist() if 'Total' not in i and 'NA' not in i and float(i)<4 ])
names = df['State'].dropna().tolist()
finalNames = []
count = 0
for i in df['Total'].dropna().tolist():
    if not 'NA' in i and not 'Total' in i:
        finalNames.append(names[count])

    count+=1
    

plt.scatter([i for i in range(1,len(finalNames)+1)],gr,label="scatter-label")
plt.xlabel("State Number when arranged alphabetically")
plt.ylabel("Distribution of Gender Ratio in institutes of that state")

plt.legend()
plt.show()
