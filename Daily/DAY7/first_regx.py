# import re
# #input1= "Ht 27 I am the 34 in 2035"
# print("Enter an input string:")
# input1=input()
# pattern='\d+'
# match=re.findall(pattern,input1)
# print("Below are the numbers in the provided string")
# print(match)



import re
def find_no_in_string(input_str):
    pattern='\d+'
    numbers=re.findall(pattern,input_str)
    return numbers


#inp_str="I am 34 in 2060 and 23"
print("Enter an input string:")
inp_str=input()
numbers=find_no_in_string(inp_str)
print(numbers)