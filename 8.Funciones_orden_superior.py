my_list=[i for i in range(1,5)]
#Map
r=list(map(lambda x:x**2,my_list))
print(my_list)
print(r)

#Filter
print('*************FILTER****************')
r=list(filter(lambda x:x%2!=0,my_list))
print(my_list)
print(r)

#Reduce
print('*************REDUCE****************')
from functools import reduce
r=reduce(lambda a,b:a+b,my_list)
print(my_list)
print(r)
