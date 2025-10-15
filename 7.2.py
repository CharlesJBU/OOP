file1 = open("test1.txt", "w") #append mode would replace the w with "A" for append
                                #"wb" stands for writein binary mode

file1.writelines("hello world!")
file1.writelines("welcome to OOP class")

file1.close()

file2 = open("test1.txt", "r")

for line in file2:
    print(line)
file2.close



