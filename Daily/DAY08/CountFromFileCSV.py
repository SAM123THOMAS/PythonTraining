def print_results(filename):
    
    Count_dict={}
    for line in file:
        line=line[:-1]
        listCreated=line.split(",")
        #print(listCreated)
        company=listCreated[1]
        if company not in Count_dict:
            Count_dict[company]=1
        else:
            Count_dict[company]+=1

    print(Count_dict)
            

file=open("D:\PythonTraining\Daily\DAY8\Sample.csv",'r')
print_results(file,)
file.close