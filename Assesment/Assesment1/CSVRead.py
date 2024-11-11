import pandas as pd        #importing pandas
file_path='D:\PythonTraining\Assesment\Assesment1\pride_And_prejudice.csv'     #defining filepath

#creating function to get word count
def  fn_Counter(filepath):
    file =open(filepath,'r',encoding='UTF-8')           #read the specified csv file
    dict_Uniquewords={}                                 #inililizing dictionay to store unique words and counts
    for line in file:                                   #looping through each files
        if line.strip()!="":                            #Checking for not empty lines                 
            line=line.strip()                           #removing spaces 
            list_Lines=line.split()                     #spliting sentences to words based on space character
            for item in list_Lines:                     #looping through each items/words in line
                if(item not in dict_Uniquewords):
                    dict_Uniquewords[item]=1            #if new word then adding to dictionary
                else:
                    dict_Uniquewords[item]+=1           #if already existing word incrementing count
    file.close()
    return dict_Uniquewords

#function call
dictUniqueWordCount =fn_Counter(file_path)

#creation of dataframe and defining columns
df=pd.DataFrame(list(dictUniqueWordCount.items()),columns=['Words', 'Count'])
print(df)   