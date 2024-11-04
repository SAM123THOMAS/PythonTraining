import pandas as pd
student_dictionary={
    "RRR":30,
    "Me. ABC":55,
    "Sam":100,
    "Libin":99
}

students=pd.Series(student_dictionary)

print(students)
print("**********************")
print(students.iloc[2])
print(students.loc['RRR'])
print("-----------------------------------")
print(students[students>50])