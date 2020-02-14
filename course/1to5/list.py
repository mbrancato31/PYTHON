num =[1,3,2,3,3,4,3,3,5,5,1,1]
uniques = []
for n in num:
    if n not in uniques:
        uniques.append(n)
print(uniques)