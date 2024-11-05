import pandas as pd
student_dictionary={
    "RRR":30,
    "Me. ABC":55,
    "Sam":100,
    "Libin":99
}

students=pd.Series(student_dictionary)
print("Sum",sum(students))
print("Max",max(students))
print('loc:',students.loc["Libin"])