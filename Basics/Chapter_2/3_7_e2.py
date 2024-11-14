guest_list = ['Mark Manson','Marilyn Manson','A Mansion']
guest_list.insert(0,'Chevy Chase')
guest_list.insert(2,'Whoopie Goldberg')
guest_list.append('Hannah Montana')

print("We're sorry ther must have been a misunderstanding, i can invite only two"
      " people for dinner")
guest_out_1 = guest_list.pop()
print(f"Dear guest {guest_out_1} you won't be attending")

guest_out_2 = guest_list.pop()
print(f"Dear guest {guest_out_2} you won't be attending")

guest_out_3 = guest_list.pop()
print(f"Dear guest {guest_out_3} you won't be attending")

guest_out_4 = guest_list.pop()
print(f"Dear guest {guest_out_4} you won't be attending")



print (f"The rest of y'all {guest_list} rr welcome")

