def say_helo(name,n):
    print("Hello "+ name)
    return name[n-1]
    

print(say_helo("Rohit",4))



def stringReverse(name):
    return name[::-1]

print(stringReverse("Rohit"))