import math
A = [1,100]
result = A[0]
for i in range(1,len(A)):
    result = math.gcd(result,A[i])
    
print(max(A)//result)






