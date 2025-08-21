# File Handeling

a = open("hello.txt", "w") # "open" 
b = 1

while b <= 10:
    a.write(str(b)+ ": Eman is a bad Girl, haha\n") # Made b str because without it, it is int and gives an error
    b = b + 1

a.close() # Close's the file 

with open ("hello.txt", "r") as f:  # In this case, the file is automatically closed when the with block is exited, regardless of whether an exception occurs or not.
    print(f.read())