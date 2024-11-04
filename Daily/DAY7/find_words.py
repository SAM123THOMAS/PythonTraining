#find words starting with specifica letter; let that be s
import re

def words_fn(inp_str):
    pattern=r'\bs\w*'
    matches=re.findall(pattern,inp_str,re.IGNORECASE)
    return matches

print("Enter an input string:")
inpt_str=input()
matches=words_fn(inpt_str)
print("Words starting with s :")
print(matches)
