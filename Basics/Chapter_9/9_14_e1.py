import random


tuple_1 = (0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','f') 

code = [random.choice(tuple_1)for i in range(4)]
codeword = ''
for char in range(len(code)):
    codeword += str(code[char])


