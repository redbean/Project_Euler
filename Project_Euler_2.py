# Python

fib = [1,2]
fib_even = []

while(fib[len(fib)-1] < 4000000):
    fib.append(fib[len(fib)-2]+fib[len(fib)-1])
    
for i in fib:
    if i%2 ==0:
        fib_even.append(i)

print sum(fib_even)
