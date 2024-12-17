import csv

with  open("favorites.csv","r") as file:
    reader = csv.reader(file)
    next(reader) # not the first line but the next line(omitting the header)
    for row in reader:
        print(row[1])

with  open("favorites.csv","r") as file:
    reader = csv.DictReader(file)# a reader that interprets the column names as dictionary keys
    
    for row in reader:
        print(row["language"])

with  open("favorites.csv","r") as file:
    reader = csv.DictReader(file)# a reader that interprets the column names as dictionary keys
    scratch,c,python = 0,0,0

    for row in reader:
        favorite = row["language"]
        if favorite == "Scratch":
            scratch += 1
        elif favorite == "C":
            c += 1
        elif favorite == "Python":
            python += 1
print(f"Scratch:{scratch}")
print(f"C:{c}")
print(f"Scratch:{scratch}")

print("\n")

#Simpler:

with open("favorites.csv") as file:
    reader = csv.DictReader(file)
    counts = {} # or counts = dict()
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1
for favorite in counts:
    print(f"{favorite}:{counts[favorite]}")
print("\n")
for favorite in sorted(counts):
    print(f"{favorite}:{counts[favorite]}")
print("\n")

for favorite in sorted(counts,key=counts.get,reverse = True):
    print(f"{favorite}:{counts[favorite]}")
    