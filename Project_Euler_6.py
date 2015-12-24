
#Project Euler Number 6

import math

n = 100
add = ((1+n)*(n/2))
mul = (n*(n+1)*((2*n)+1))/6

print math.pow(add,2) - mul
