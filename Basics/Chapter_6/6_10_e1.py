favorite_numbers = {'Mia':1, 'Saul': [11,12,13], 'Fran': 3, 'Mike': 7, 'Slevin': [18,21]}
for person,numbers in favorite_numbers.items():
    if numbers != int:
        print(f"{person}'s favorite numbers are {favorite_numbers[person]}.")
    elif numbers == list:
        print(f"{person}'s favorite number is {numbers}")


