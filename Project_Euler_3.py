i=2
tar = 600851475143
while 1:
    if i % 2 != 0 and i % 3 !=0 and i % 5 !=0 and i % 7 !=0 or i ==5 or i==7:
        while tar%i==0:
            tar = tar/i
            print i
    i = i+1
