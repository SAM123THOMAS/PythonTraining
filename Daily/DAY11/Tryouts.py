#Print firts 5 of Age column
import pandas as pd
df=pd.read_csv(r"D:\PythonTraining\Daily\Titanic\titanic.csv")
#print(df['Age'].head())

#Create a subset of dataframe with only 2 columns 'Age', 'Sex'
#Print first 5 rows

#print(df[['Age','Sex']].head())


#filter out all the peeople with age less than 25 and print

#print(df[df['Age']<25])

#how many rows does my data have
print(len(df.index))

#Average age
print("Average",df['Age'].mean())

#Get the avrerage fare of all the male passenges whose age<25

df_filt=df[(df["Sex"]=='male')&(df["Age"]<25)]
#print(df_filt)
print(df_filt["Fare"].mean())

#df_filt.to_csv("Filtered.csv",index=False)

#What percentage of the passengers survived the titanic
dt_survived=df[df['Survived']==1]
surv_count=len(dt_survived.index)
total_count=len(df.index)
percentage=(surv_count/total_count)*100
print("Percentage",percentage)


