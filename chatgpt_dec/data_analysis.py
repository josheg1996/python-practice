import pandas as pd

#Load .csv file as a dataframe
df = pd.read_csv("data.csv")
print(df)

#Display first five rows
print("First five rows",df[0:5])

#Display no. rows, columns
rows = df.shape[0]
columns = df.shape[1]
print("rows: %d columns: %d" %(rows,columns))

#Calculate average salary
s= df['Salary'].tolist()
salaries = []
for i in range(0,len(s)):
    salaries.append(int(s[i]))
    
ave_salary = sum(salaries)/len(salaries)
print('Average salary is: ', ave_salary)

#Find highest salary
for i in range(0,len(salaries)):
    if salaries[i] == max(salaries):
        z = i
print("Highest Earner")
print(df.iloc[z])

#Group Average Salary by Department
dep = df['Department'].tolist()
d = []
for i in dep:
    if i not in d:
        d.append(i)
print(d)
y = [0]*len(d)
c = [0]*len(d)
res = []
for i in range(len(d)):
    for j in range(len(dep)):
        if dep[j]==d[i]:
            y[i]+=salaries[j]
            c[i] += 1
    res.append(y[i]/c[i])
print("Average Salary By Department")
print(d)
print(res)

