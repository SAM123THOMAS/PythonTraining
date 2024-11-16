import pandas as pd
df=pd.read_csv(r"D:\PythonTraining\Daily\Titanic\titanic.csv")

#1. Compare the average age of passengers who survived with those who didn't

# avg_age_survived=df[df["Survived"]==1]["Age"].mean()
# print(avg_age_survived)
# avg_age_Notsurvived=df[df["Survived"]==0]["Age"].mean()
# print(avg_age_Notsurvived)

#2.Calculate the survival rate by gender
# df_survivalRate=df.groupby("Sex")["Survived"].mean().reset_index()
# print(df_survivalRate.rename({"Survived":"Survival Rate"}))

#3.Family size

df["Family Size"]=df["SibSp"]+df["Parch"]
#print(df[["SibSp","Parch","Family Size"]].head())

#3.1 calculate average survival rate by family size then
#3.2 merge the family survival rate back into the original dataframe
#3.3 display the resulting dataframe

df_averag_survival_rate=df.groupby("Family Size")["Survived"].mean().reset_index()
df_averag_survival_rate.columns=['Family Size','Family_Survival_Rate']
print(df_averag_survival_rate)

df_mergFamily=pd.merge(df,df_averag_survival_rate,on="Family Size",how="left").reset_index()
print(df_mergFamily[["Family Size",'Family_Survival_Rate']].head(10))


