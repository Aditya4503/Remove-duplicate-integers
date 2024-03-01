def remdup(l):
    for i in range(len(l)):
        for j in range(len(l)):       
            if l[i]==l[j] and i<j:
                l.pop(j)
                l.insert(0,"")
                
    for i in range(len(l)):
        if isinstance(l[0],str):
            l.remove(l[0])
    print(l)

remdup([5,5,5,5,1,1,5,5,5])