def print_results(filename,target_school):
    

    for line in file:
        line=line[:-1]
        listCreated=line.split(",")
        #print(listCreated)
        if(listCreated[1]==target_school):
            print(line)

file=open("D:\PythonTraining\Daily\DAY8\Sample.csv",'r')
print_results(file,"UST")
file.close
