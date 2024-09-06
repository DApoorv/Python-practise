class operations:
    def __init__(self):
        self.name = ["", "Bob", "Rebecca", "Clint", "11231", "32173"]
    def data (self, names):
        self.names = list(filter (lambda el:el[0].isupper() and el[1:].islower (), names)) 
        return self.name
    def display(self, result):
        length= len(''.join(self.names))
        n = sorted([int(x) for x in result if x.isdigit()])
        for i in ((filter (lambda x:x>length,n))):
            return i

o = operations()
names = ['Alice', 'mark Thomas', 'rebecca', 'Bob1231', '08732', 'Clint', "11231", "32173"]
result = o.data(names)
dis = o.display(result)
print(dis) # 11231

##################
import pandas as pd
index = pd.IntervalIndex.from_arrays([1,3,5],[12,24,36])
data = [10,20,30]
s = pd.Series(data, index=index)
print(s)
print(s.loc[1.5]) # 10

#########################
def compare(a, b):
    if a == b:
        return True
    else:
        return False

def remove_extra(a):
    for i in a:
        if i not in b:
            b.append(i)
            a.remove(i)
    print(b)

a = [1,1,2,2,3,4,4,3,0,0]
b = []
remove_extra(a)
print(compare(a, b)) 
# [1,2,3,4,0]
# False

################
s = pd.Series([7,2,8,3,1])
print(s)
s_i = s.argsort()
print(s_i)
s_v = s.loc[s_i[::-1]]
print(s_v)

#####################


arr = np.array([[7,8,9],[4,5,6]])
result = np.square(arr)
for row in result:
    for num in row:
        print(num, end=" ")
    print()
# 49 64 81 
# 16 25 36 


###################
#Need to correct it
import numpy as np
arr_1=([1,4,9,16], [25,39,25,2,3], [1,54,96,236,458])
arr=np.array(arr_1)
arr_2= np.array([1,23,4545,3,5,5648])
for array in arr.flat:
    print(array)
print(arr_2.argmax (axis=0), arr.argsort())
print(arr.ndim, arr_2.nbytes, arr_2.reshape(3,2)) 
print(arr_2.argmin (axis=1))
