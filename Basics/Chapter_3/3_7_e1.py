guest_list = ['Mark Manson','Marilyn Manson','A Mansion']
print(f"Thee honourable guest {guest_list[0].title()} is hereby invited to dinner at 5 o'clock")
print(f"Thee honourable guest {guest_list[1].title()} is hereby invited to dinner at 5 o'clock")
print(f"Thee honourable guest {guest_list[2].title()} is hereby invited to dinner at 5 o'clock")

print(f"Unfortuantely the guest {guest_list[2].title()} will not be able to grace us with it's presence at it is stationary.")
guest_list[2] = 'A boat'

print(f"Thee honourable guest {guest_list[0].title()} is hereby invited to dinner at 5 o'clock")
print(f"Thee honourable guest {guest_list[1].title()} is hereby invited to dinner at 5 o'clock")
print(f"Thee honourable guest {guest_list[2].title()} is hereby invited to dinner at 5 o'clock")


print(f"Hear thee we found a bigger table")
guest_list.insert(0,'Pascal Sauvage')
guest_list.insert(2,'Lady Sinclair')
guest_list.append('Loco Moco')

print(f"Thee honourable guest {guest_list[0].title()} is hereby invited to dinner at 5 o'clock")
print(f"Thee honourable guest {guest_list[1].title()} is hereby invited to dinner at 5 o'clock")
print(f"Thee honourable guest {guest_list[2].title()} is hereby invited to dinner at 5 o'clock")
print(f"Thee honourable guest {guest_list[3].title()} is hereby invited to dinner at 5 o'clock")
print(f"Thee honourable guest {guest_list[4].title()} is hereby invited to dinner at 5 o'clock")
print(f"Thee honourable guest {guest_list[5].title()} is hereby invited to dinner at 5 o'clock")

print(f"Hear thee the bigger table will not arrive")

guest_gone = guest_list.pop()
print(f"we inform you not to oblige us with your presence guest {guest_gone}\n")
guest_gone = guest_list.pop()
print(f"we inform you not to oblige us with your presence guest {guest_gone}\n")
guest_gone = guest_list.pop()
print(f"we inform you not to oblige us with your presence guest {guest_gone}\n")

print(f"Thee honourable guest {guest_list[0].title()} is hereby invited to dinner at 5 o'clock, invitation is still valid")
print(f"Thee honourable guest {guest_list[1].title()} is hereby invited to dinner at 5 o'clock, invitation is still valid")
print(f"Thee honourable guest {guest_list[2].title()} is hereby invited to dinner at 5 o'clock, invitation is still valid")


del guest_list[0]
del guest_list[0]
del guest_list[0]
print(guest_list)
