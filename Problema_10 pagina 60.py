m=set({'1','2','3','4'})
n=set({'1','2','3','4'})
for x in m:
    for y in m:
        n.add(x+y)
for z in m:
    n.add(x+y+z)
for w in m:
    n.add(x+y+z+w)
print(*n)

