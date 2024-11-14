import statistics
from statistics import mean


one_million_list = []

for i in range(1_000_000):
    one_million_list.append(i)

#print(one_million_list)

print(one_million_list.pop())

for i in one_million_list:
    #print(i)
    print(mean(one_million_list))
    if i == i:
        break
