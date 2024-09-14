mac = {'first_name':'mac','last_name':'skonc','age':38,'city':'wwa'}

#for datapoint in mac:
 #   print(mac[datapoint])

bill = {'first_name':'bill','last_name':'jones','age':23,'city':'Cancun'}

david = {'first_name':'david','last_name':'morenas','age':35
         ,'city':'Houston'}


people = [mac,bill,david]

for person in people:
    print(f'The first person\'s name is {person['first_name'].title()}.')
    print(f'The first person\'s last name is {person['last_name'].title()}.')
    print(f'The first person is {person['age']}.')
    print(f'The first person lives in {person['city']}.\n')




