import random


tuple_1 = (0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','f') 

code = [random.choice(tuple_1)for i in range(4)]
codeword = ''
for char in range(len(code)):
    codeword += str(code[char])


#print(code)
#print(f"Any ticket matching this set of numbers and letter wins: {codeword}!!!")


my_tuple_1 = (0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','f') 


my_codeword = ''
attempts = 0

while my_codeword != codeword:
    my_code = [random.choice(tuple_1)for i in range(4)]
    my_codeword = ''.join(str(char) for char in my_code)
   # for char in range(len(my_code)):
    #    my_codeword += str(my_code[char])
    attempts += 1



print(code)
print(f"Any ticket matching this set of numbers and letter wins: {codeword}!!!")
print(f"It took {attempts} attempts to match the winning code.")

