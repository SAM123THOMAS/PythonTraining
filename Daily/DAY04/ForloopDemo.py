## write a for loop to print users name multiple times

def print_name(name_input, num_input):
    print("Loop starts - ")
    for i in range(int(num_input)):
        print(i + 1,name_input)

print ("Hello user, what is your name")
name_input = input()
print ("How many times you want to see your name")
num_input = input()
print_name(name_input,num_input)