test = []

for i in range(999,600, -1):
    for j in range(999,600, -1):
        mul = i*j      
	if str(mul)[:len(str(mul))/2] == (str(mul)[len(str(mul))/2:])[::-1]:
	    test.append(mul)
				        

print test[0]
