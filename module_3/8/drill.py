numbers = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

sublist = {}
keys = ["A", "B", "C", "D"]
for row in numbers:
    sublist[keys[0]] = row
    keys.remove(keys[0])
    if row[0] != 0:
        for element in row:
            if element != 0:
                print(element)
        
print(sublist)