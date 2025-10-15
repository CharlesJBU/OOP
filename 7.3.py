import pickle

d = {"stu1": {"name":"John", "age":"21", "id":"28"},
     "stu2":{"name":"bob", "age":"30", "id":"27"},}
with open("myUsers.dat", "wb") as file1:
    pickle.dump(d, file1)
file1.close()

with open("myUsers.dat", "rb") as file2:
    myDictionary = pickle.load(file2)

print(myDictionary)
print(myDictionary["stu1"]["name"])

i = 1
for x in myDictionary:
    var = "stu"+str(i)
    print(myDictionary[var]["name"])
    i +=1
print(myDictionary[var]["name"])