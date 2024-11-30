n = int(input("Input n:"))

def digital_root(n):
    string_n = str(n)
    digital_root = 0
    while n > 10:
        for char in string_n:
            digital_root += int(char)
            n = digital_root
        return digital_root
        return n
    

print(digital_root(n))

