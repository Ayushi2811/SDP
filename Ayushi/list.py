#first list
l={'python','c','java'}
print(l)


#neat list
l={'python','c','java'}
for i in l:
    print("A nice programing language is",i)
    
    #message list
l={'Pink','Blue','Black','White'}
for i in l:
    print("Item in the list is",i)
    
    #for loop
l={'python','c','java'}
for i in l:
    print(i)
    
    #working list
l=['programmers','doctors','drivers','chef']
l.index('chef')
if 'doctors' in l:
    print("Yes it is present")
l.append('teacher')
print(l)
l.insert(0,'barber')
print(l)
for i in l:
    print(i)
    
    #starting form empty
l=[]
l.append('doctor')
l.append('author')
l.append('detective')
l.append('engineer')
res=[l[0],l[-1]]
print(res)


#ordered working list
l=['programmers','doctors','drivers','chef']
print("original order:")
for i in l:
    print(i)
print("sorted list:")
for i in sorted(l):
    print(i)
print("original:")
for i in l:
    print(i)
print("Reverse:")
l.reverse()
for i in l:
    print(i)
print("original")
print(l)


#alphabet slices
l=['a','b','c','d','e','f','g','h']
print(l[0:3])
print(l[4:])

