#title:Item counter
#author: michael stoll
#date: 3/24/2025
with open("names.txt", "r") as f:
    lines = f.readlines()

names = 0

for line in lines:
    names += 1
print(names, "names in file")